from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "API E-Commerce IRESM"
    DATABASE_URL: str
    CORS_ORIGINS: str = "http://localhost:5173,http://127.0.0.1:5173"

    # Variables de Auth
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_MIN: int = 30
    REFRESH_MIN: int = 10080

    @property
    def origins(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()