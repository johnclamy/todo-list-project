import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/books')
def root() -> dict[str, str]:
    return {"msg": "book list will go here"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
