from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    return "hi"


@app.get("/1")
def welcome2():
    return "1"


@app.get("/2")
def welcome3():
    return "you entered {}"
