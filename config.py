from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Pydantic автоматически соберет эти переменные из ОС или .env
    DB_HOST: str
    DB_PORT: int = 5432
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Указываем считывать настройки из файла .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
