from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/items/{item_id}')
async def hello_param(item_id):
    return {'message': f'Hello id: {item_id}'}
