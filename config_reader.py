from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TOKEN_API: SecretStr
    ADMIN_USER_ID: SecretStr

    model_config = SettingsConfigDict(env_file='env_dist.env', env_file_encoding='utf-8')


config = Settings()
