import hashlib
import json
import numpy as np

def hash_face_vector(vector):
    # Converte para NumPy array
    vec = np.array(vector)

    # Normaliza o vetor
    norm_vector = vec / np.linalg.norm(vec)

    # Converte para string JSON
    vector_string = json.dumps(norm_vector.tolist())

    # Gera o hash SHA-256
    return hashlib.sha256(vector_string.encode("utf-8")).hexdigest()
