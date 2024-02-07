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

@app.post("/cargarDocumento/{bl}/{idOrden}")
async def cargarDocumento(bl,idOrden,files: List[UploadFile] = File(...)):
    listdocs = []
    try:
        # for file in files:
        #     print(file.filename)
        #     with open(file.filename, 'wb') as myfile:
        #         content = await file.read()
        #         myfile.write(content)
        #         myfile.close()

        #         if not os.path.exists('documentos/'+str(idOrden)+''):
        #             os.mkdir('documentos/'+str(idOrden)+'')
            file = await files.read()
            return {"nombre": file.filename, "tamaño": len(files)}
    except Exception as e:
        print(e)
        return {'Res':e}