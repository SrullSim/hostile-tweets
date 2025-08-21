from fastapi import FastAPI
import uvicorn
import os
from manager import Manager


app = FastAPI()
manager = Manager()

@app.get("/get_data")
async def get_data():
    return manager.get_df_as_list_of_json()


if __name__ == "__main__":
    uvicorn.run(app , host="0.0.0.0", port=8080)