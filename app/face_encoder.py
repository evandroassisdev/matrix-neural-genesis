from insightface.app import FaceAnalysis
import numpy as np
import cv2

# Usa o diretório local onde o modelo já está salvo
model = FaceAnalysis(name="buffalo_l", root="./models")
model.prepare(ctx_id=0)

def get_face_vector(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faces = model.get(img_rgb)
    if len(faces) == 0:
        print("🚫 No face detected.")
        return None
    elif len(faces) > 1:
        print(f"⚠️ {len(faces)} faces detected. Please provide only one.")
        return None

    print("✅ One face successfully detected.")
    embedding = faces[0].embedding
    return embedding.tolist()
