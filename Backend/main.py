from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():

    data = {"message": "JobTrack API"}
    return data