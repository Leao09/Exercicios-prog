import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.responses import FileResponse, StreamingResponse
import os
from supabase import create_client, Client
import asyncio
import aiofiles
import time
app = FastAPI()
# URL e Chave de acesso
url: str = "https://madnwqvnjqeupsynmlbo.supabase.co"

key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1hZG53cXZuanFldXBzeW5tbGJvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NjcxNDI5MSwiZXhwIjoyMDAyMjkwMjkxfQ.gKI4JzzZA8atUMlqUb-_O6gFyQNYDLidsl3VNlQ3fCg"
supabase: Client = create_client(url, key)
#Nome do bucket utilizado
bucket_name: str = "exercicioprog1"
list_files = os.listdir("recebidos")
@app.get("/list")
async def list():
    # Lista todas as imagens do Bucket
    res = supabase.storage.from_(bucket_name).list()
    print(res)

@app.post("/upload")
def upload(content: UploadFile = fastapi.File(...)):
    with open(f"recebidos/rachadura{time.time()}.png", 'wb') as f:
        dados = content.file.read()
        f.write(dados)
        #pass
    return {"status": "ok"}

@app.post("/images")
def images():
    # Rota da imagem local para ser feito o upload (no meu caso esta na pasta mock e é a imagem "lala.png")
    for arquivo in list_files:
        with open(os.path.join("recebidos", arquivo), 'rb+') as f:
            dados = f.read()
            res = supabase.storage.from_(bucket_name).upload(f"{time.time()}_{arquivo}", dados)
    return {"message": "Image uploaded successfully"}



