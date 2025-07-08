from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import time

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


@app.get("/stress")
async def get_stress():
    end_time = time.time() + 20
    while time.time() < end_time:
        x = 0
        for i in range(10000):
            x += i ** 2
    return {"port": f"Stress in port: {PORT}"}
