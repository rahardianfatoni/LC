from fastapi import FastAPI
import pandas as pd
import uvicorn

app = FastAPI()

df = pd.read_csv("E:/Download/rahardiansyah_fatoni.csv")
df = df.to_dict()

@app.get('/')
def home():
    return {"message": "Welcome"}

@app.get('/display')
def display():
    return df

if __name__ == "__main__":
    uvicorn.run('rahardiansyah-fatoni_app:app', host="127.0.0.1", port=8000, reload=True)