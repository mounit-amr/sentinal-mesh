from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def value():
    return {"online"}
    