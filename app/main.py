from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

PORT = os.getenv("PORT", "8000")
app = FastAPI()


@app.get("/test")
def listar_usuarios():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"}, status_code=200)


@app.get("/port")
async def get_port():
    return {"port": PORT}
