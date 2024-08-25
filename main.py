from contextlib import asynccontextmanager

from fastapi import FastAPI




from config.general import settings


from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:3000"
    ]

app = FastAPI()

