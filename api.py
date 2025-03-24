from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import base64
import numpy as np
from datetime import datetime, timezone

from app.database import faces_collection
from app.verifier import calculate_similarity
from app.hash_generator import hash_face_vector
from app.face_encoder import get_face_vector
from app.utils import save_temp_file

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Matrix Neural Identity API is running."}


@app.post("/register_smart")
async def register_face(file: UploadFile = File(...)):
    temp_path = save_temp_file(file)
    vector = get_face_vector(temp_path)

    if vector is None:
        os.remove(temp_path)
        return JSONResponse(status_code=400, content={"error": "No valid face found"})

    vector_np = np.array(vector)
    best_match = None
    best_similarity = 0.0

    # 🔍 Verifica similaridade com identidades existentes (usando vetor médio)
    for idx, doc in enumerate(faces_collection.find()):
        vectors = doc.get("vectors", [])
        if vectors:
            avg_vector = np.mean(np.array(vectors), axis=0)
            similarity = calculate_similarity(vector_np, avg_vector)
            print(f"🧠 Similaridade com identidade #{idx + 1}: {round(similarity, 2)}%")

            if similarity > best_similarity:
                best_similarity = similarity
                best_match = doc

    # 🧠 Define limite de similaridade (ajustável)
    threshold = 70.0

    # 🖼️ Converte imagem para base64
    with open(temp_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    if best_match and best_similarity >= threshold:
        updated_vectors = best_match.get("vectors", [])[-2:]  # mantém os 2 últimos
        updated_vectors.append(vector_np.tolist())

        faces_collection.update_one(
            {"_id": best_match["_id"]},
            {
                "$set": {
                    "vectors": updated_vectors,
                    "image_sample": image_base64
                }
            }
        )
        
        os.remove(temp_path)
        return JSONResponse(status_code=200, content={
            "message": "Face already registered (new vector added)",
            "similarity": round(best_similarity, 2),
            "hash": best_match["hash"]
        })

    # 🔐 Gera nova identidade se nenhuma correspondente for encontrada
    face_hash = hash_face_vector(vector_np.tolist())
    faces_collection.insert_one({
        "hash": face_hash,
        "vectors": [vector_np.tolist()],
        "image_samples": [image_base64],
        "created_at": datetime.now(timezone.utc)
    })

    os.remove(temp_path)

    return JSONResponse(status_code=200, content={
        "message": "New face identity registered",
        "hash": face_hash
    })


@app.get("/faces")
def get_all_faces():
    total = faces_collection.count_documents({})
    return {"registered_identities": total}