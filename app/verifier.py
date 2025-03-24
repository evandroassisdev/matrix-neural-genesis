import numpy as np

def calculate_similarity(vec1, vec2):
    """
    Calculates cosine similarity between two vectors and returns the value in percentage (0–100%).
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    sim = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    return round(float(sim) * 100, 2)
