from pymongo import MongoClient
import os

# Lê URI do MongoDB das variáveis de ambiente
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)
db = client["database_name"]  # Nome do banco de dados
faces_collection = db["faces"]  # Nome da coleção onde as faces serão salvas
