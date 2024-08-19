from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str
    DATABASE_NAME: str

    class Config:
        env_file = ".env"


def load_settings():
    try:
        settings = Settings()
    except FileNotFoundError:
        settings = Settings(_env_file=None)

    return settings


settings = load_settings()
