# app/utils.py
import uuid
import os

def save_temp_file(upload_file):
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, f"{uuid.uuid4()}.jpg")
    with open(temp_path, "wb") as f:
        f.write(upload_file.file.read())
    return temp_path
