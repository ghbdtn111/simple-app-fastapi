import uvicorn
from routers import users
from fastapi import FastAPI


app = FastAPI(
    title='simple app',
)

app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello!!!"}


if __name__ == "__main__":
    import sys
    from os.path import abspath, dirname

    sys.path.insert(0, dirname(abspath(abspath(__file__))))
    uvicorn.run(app, host="127.0.0.1", port=8000)
