from fastapi import FastAPI
import uvicorn

from api.train_api import router as train_router
from api.station_api import router as station_router
from api.incident_api import router as incident_router

app = FastAPI(
    title="PRASA Smart Digital Monitoring System",
    version="1.0"
)

app.include_router(train_router)
app.include_router(station_router)
app.include_router(incident_router)

@app.get("/")
def home():
    return {"message": "PRASA API Running"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)