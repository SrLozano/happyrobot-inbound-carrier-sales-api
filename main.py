from dotenv import load_dotenv
from fastapi import FastAPI

from api.routes import carriers, loads

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Inbound Carrier Sales API",
    description="API for verifying carriers and searching for freight loads, built for Acme Logistics.",
)

# Include the routers from the routes module
app.include_router(carriers.router)
app.include_router(loads.router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Inbound Carrier Sales API"}
