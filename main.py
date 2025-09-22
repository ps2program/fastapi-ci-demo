
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, GitHub Actions!, Prahlad"}

@app.get("/square/{number}")
def square_number(number: int):
    return {"number": number, "square": number * number}
