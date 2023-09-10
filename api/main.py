from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)


@app.get('/')
async def root():
    return {'message': 'Server is running successfully'}


@app.get('/message')
async def root():
    return {'message': 'Server api at /message '}
