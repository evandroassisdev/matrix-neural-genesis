# 🧠 Matrix Neural Genesis

Facial identity system powered by neural recognition, secure hash registration, and intelligent similarity verification with decentralized storage support.

---

## 🚀 Technologies Used

- **FastAPI** – Lightweight modern API backend
- **MongoDB** – Database for storing face vectors, hashes, and images
- **InsightFace (ArcFace)** – Deep learning model for face embeddings
- **Docker & Docker Compose** – Containerized development and deployment
- **Python 3.10**
- **Uvicorn** – ASGI server for FastAPI

---

## 🧬 How It Works

1. The user uploads a **selfie**
2. The system detects and aligns the face
3. An **embedding (vector)** is generated using ArcFace
4. It compares the new vector with existing identities in the database
5. If similarity ≥ 70%, the vector is added to the existing identity
6. Otherwise, a **new identity** is created
7. Each identity contains:
   - Unique hash (SHA-256 of the average vector)
   - Up to 3 vectors (to represent variations)
   - One image sample (stored as base64)

---

## 🧪 Local Testing with Docker

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 1. Clone the repository

```bash
git clone https://github.com/your-user/matrix-neural-genesis.git
cd matrix-neural-genesis
