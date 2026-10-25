from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Welcome to AI Job Assistant"}

@app.get("/health")
def health_check():
    return{"status":"ok"}