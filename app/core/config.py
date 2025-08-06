from pydantic import ValidationError
from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path
import os, tempfile


class Settings(BaseSettings):
    DATABASE_URL: str  # DSN as plain string
    DB_CA_CERT: str # DB certificate as plain string

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        

settings: Settings = Settings() # pyrefly: ignore(missing-argument)


def get_ca_file() -> Path | None:
    if not settings.DB_CA_CERT:
        return None

    # Create a temp file under /tmp
    tmp: Path = Path(tempfile.mkstemp(suffix=".crt")[1])
    tmp.write_text(settings.DB_CA_CERT)
    # Restrict permissions: -rw-------
    os.chmod(tmp, 0o600)
    return tmp
