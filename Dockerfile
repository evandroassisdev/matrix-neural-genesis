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
  unzip \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 🔽 Instala o gdown (via pip)
RUN pip install gdown

COPY . .

# 🔽 Baixa o models.zip do Google Drive (com bypass de verificação) e extrai
RUN gdown https://drive.google.com/uc?id=12aoLkLp_Kw1XyIbm5j4Fp6bapNhSoYn0 && \
  unzip models.zip -d ./models && \
  rm models.zip

EXPOSE 8000

CMD ["python", "main.py"]
