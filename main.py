from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_customers(customers):
    return customers


@app.post("/")
def add_customers(customers):
    return customers
