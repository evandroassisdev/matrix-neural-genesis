# Dockerfile
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
  build-essential \
  cmake \
  libopenblas-dev \
  liblapack-dev \
  libx11-dev \
  libgtk-3-dev \
  libboost-python-dev \
  libboost-system-dev \
  libboost-thread-dev \
  libboost-iostreams-dev \
  libboost-filesystem-dev \
  git \
  curl \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# ✅ Copia os modelos baixados para dentro do container
COPY models ./models

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
