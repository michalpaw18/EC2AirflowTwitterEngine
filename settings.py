import os
from dotenv import find_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BEARER_TOKEN: str = Field(
        ...,
        description="",
    )

    ACCESS_KEY: str = Field(
        ...,
        description="",
    )

    ACCESS_SECRET: str = Field(
        ...,
        description="",
    )

    CONSUMER_KEY: str = Field(
        ...,
        description="",
    )

    CONSUMER_SECRET: str = Field(
        ...,
        description="",
    )

    class Config:
        env_file = find_dotenv()


SETTINGS = Settings()