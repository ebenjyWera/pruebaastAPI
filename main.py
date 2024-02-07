import json
import os
import shutil
from typing import Union
from typing import Union, List
from fastapi import FastAPI, UploadFile, File
from datetime import datetime, timedelta
# from clases import Usuario,Conexion,Ordenes,Documentos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/documento/")
async def crear_documento(documento: UploadFile = File(...)):
    contenido = await documento.read()
    return {"nombre": documento.filename, "tamaño": len(contenido)}