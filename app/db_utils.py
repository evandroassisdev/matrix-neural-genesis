import base64
from app.db import faces_collection

def save_face_record(face_hash, vector, image_path):
    # Converte imagem em base64
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

    document = {
        "hash": face_hash,
        "vector": vector,
        "image": encoded_image
    }

    result = faces_collection.insert_one(document)
    return str(result.inserted_id)
