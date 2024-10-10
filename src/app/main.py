from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.database import Base, engine
from core.config import settings
from api.v1.endpoints import products, sales


app = FastAPI(
    title=settings.app_name,
    version=settings.version_api,
    description=settings.description_api,
    redoc_url=None,
)

# Configuração do CORS
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(
    router=products.router,
    prefix='/products',
    tags=['Produtos']

)

app.include_router(
    router=sales.router,
    prefix='/sales',
    tags=['Vendas']
)


@app.get('/check')
def healthcheck():
    return {
        "status": "API em funcionamento normal",
        "version": settings.version_api
    }