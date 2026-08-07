from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "radar"
    app_env: str = "development"
    database_url: str = ""
    redis_url: str = ""


settings = Settings()
