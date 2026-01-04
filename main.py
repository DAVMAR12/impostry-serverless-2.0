from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Привет, Давид, я Криштиану Роналду!"}