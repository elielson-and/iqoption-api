FROM python:3.7

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo requirements.txt para o container
COPY requirements.txt .

# Instala as dependências especificadas em requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código-fonte para o diretório de trabalho
COPY . .

# Executa o script principal
CMD ["python", "main.py"]