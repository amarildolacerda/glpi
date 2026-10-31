from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "glpi-ai-support"
    app_version: str = "0.1.0"
    environment: str = "development"


settings = Settings()
