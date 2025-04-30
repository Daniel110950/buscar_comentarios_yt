# Usa imagem base leve com Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . .

# Instala as dependências da API do YouTube
RUN pip install --no-cache-dir google-api-python-client

# Comando para rodar o script
CMD ["python", "buscaComentariosYoutube.py"]
