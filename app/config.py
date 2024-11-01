from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv(".env"))


class BaseConfig(BaseSettings):
    """Base settings."""

    OPENAI_API_KEY: str | None = None
    model_config = SettingsConfigDict(env_file=find_dotenv(".env"), extra="ignore")
