#!/bin/bash

echo "🚀 Construindo e iniciando os containers com Docker Compose..."

# Para garantir que tudo esteja limpo
docker compose down --remove-orphans
docker volume rm matrix-neuralgenesis_mongodb_data 2>/dev/null

# Sobe tudo novamente
docker compose up --build
