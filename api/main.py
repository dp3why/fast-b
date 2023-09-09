from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/{name}')
async def hello_param(name):
    return {'message': f'Hello {name}'}
