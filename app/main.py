from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, PhamZero! FastAPI is running 🚀"}

@app.get("/status")
def get_status():
    return {"status": "ok", "system": "PhamZero Template V2.0"}
