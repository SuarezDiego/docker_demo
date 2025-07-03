from fastapi import FastAPI


app = FastAPI()


@app.get("/test")
def listar_usuarios():
    return {"message": "Hello, World!"}
