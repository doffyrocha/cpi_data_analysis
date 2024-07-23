from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/data")
def get_data():
    df = pd.read_csv("cpi_data.csv")
    return df.to_dict()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
