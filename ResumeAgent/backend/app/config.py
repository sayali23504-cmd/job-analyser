from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AG CloudCore - Resume Intelligence Agent V1"
    app_version: str = "1.0.0"
    api_prefix: str = "/api/v1"

    openai_api_key: str = ""
    openai_model: str = "gpt-4.1-mini"

    root_dir: Path = Path(__file__).resolve().parents[2]
    data_dir: Path = root_dir / "data"
    output_dir: Path = data_dir / "outputs"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
