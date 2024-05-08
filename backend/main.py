from database.database import DataBase
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app: FastAPI = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
    allow_origins=['http://localhost:3000']
)

@app.get('/teste')
async def teste():
    database: DataBase = DataBase()
    database.cursor.execute(
        """
        SELECT * FROM carro;
        """
    )
    data: list = database.cursor.fetchall()
    return {'dados': data}

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=7777)
