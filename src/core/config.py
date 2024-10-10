import os
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl

class Settings(BaseSettings):
    # API and documentations configurations
    app_name: str = "API Shopping"
    version_api: str = "0.0.1"
    admin_mail: str = "admin@shopping"
    description_api: str = "API para gestão de estoques e vendas."
    api_prefix: str = "api/v1"

    base_url: AnyHttpUrl = "https://localhost:3001"

    # message errors
    message_unauthorized: str = 'Você não tem permissão para acessar este recurso.'
    message_invalid_token: str = 'Token inválido ou expirado.'
    message_product_not_found: str = 'Produto não encontrado.'
    message_insufficient_stock: str = 'Estoque insuficiente para prosseguir.'

    # JWT Configuration
    secret_key: str = '122333444455555666666777777788888888'
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 30

    # Database configurations
    data_base_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.sqlite3")

    class Config:
        env_file = "./env"

settings = Settings()