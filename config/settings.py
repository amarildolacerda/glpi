import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

if (BASE_DIR / ".env").exists():
    load_dotenv(BASE_DIR / ".env", override=False)
else:
    load_dotenv(BASE_DIR / ".env_default", override=False)


def _get_bool_env(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "glpi-ai-support")
    app_version: str = os.getenv("APP_VERSION", "0.1.0")
    environment: str = os.getenv("APP_ENVIRONMENT", "development")
    glpi_base_url: str = os.getenv("GLPI_BASE_URL", "https://glpi.example")
    glpi_api_token: str = os.getenv("GLPI_API_TOKEN", "")
    auto_pilot_enabled: bool = _get_bool_env("AUTO_PILOT_ENABLED", True)


settings = Settings()
