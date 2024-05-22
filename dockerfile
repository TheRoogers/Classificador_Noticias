# imagem base do Python
FROM python:3.9-slim

# diretório dentro do container
WORKDIR /app

# Copie os arquivos para o diretório dentro do contêiner
COPY . .

# Instalando as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Porta em que a aplicação Flask está sendo executada
EXPOSE 5000

# Comando para executar a aplicação Flask
CMD ["python", "app.py"]
