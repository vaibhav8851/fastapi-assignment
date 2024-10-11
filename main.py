from fastapi import FastAPI
from routes.items import router as items_router
from routes.clock_in import router as clock_in_router

app = FastAPI()

app.include_router(items_router)
app.include_router(clock_in_router)
