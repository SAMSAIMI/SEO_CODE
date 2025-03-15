from pydantic_settings import BaseSettings
from pydantic import EmailStr
from typing import List


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI for SEO Portal"

    SECRET_KEY: str = "seo-portal-09d25e094f-aa6ca2556c8-18166b7a9563b93f708f"   # also use for JWT_SECRET_KEY
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 15

    CORS_ORIGINS: List[str] = ["http://localhost:3000", "localhost:3000"]

    MONGODB_URL: str = "mongodb://localhost:27017"
    DB_NAME: str = "seodb"

    class Config:
        case_sensitive = True

settings = Settings()


class EmailSettings(BaseSettings):
    SMTP_TLS: bool = True
    SMTP_PORT: int = 587
    SMTP_HOST: str = "smtp.office365.com"
    SMTP_USER: str = "orbops@measat.com"
    SMTP_PASSWORD: str = "P@ssw0rd123"
    EMAILS_FROM_NAME: str = "SEO Portal"
    EMAILS_FROM_EMAIL: EmailStr = "orbops@measat.com"

    class Config:
        case_sensitive = True

email_settings = EmailSettings()

