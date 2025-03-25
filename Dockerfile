FROM python:3.10-slim
ARG ENV=production
ENV ENV=${ENV}

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

RUN pip install gdown

COPY . .

# 🔽 Só baixa e extrai o modelo se estiver em produção
RUN if [ "$ENV" = "production" ]; then \
  echo "🔽 Download models" && \
  gdown https://drive.google.com/uc?id=12aoLkLp_Kw1XyIbm5j4Fp6bapNhSoYn0 && \
  unzip -o models.zip -d ./models && \
  rm models.zip ; \
  else \
  echo "🧪 Ambiente de desenvolvimento - usando models locais" ; \
  fi

EXPOSE 8000

CMD ["python", "main.py"]
