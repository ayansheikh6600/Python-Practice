from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/validate/{age}")
def validate_age(age: int):
    if age < 18:
        raise HTTPException(status_code=400, detail="You must be 18 or older.")
    return {"age": age}