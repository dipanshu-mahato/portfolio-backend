from typing import Generator, Any
import ssl, pathlib
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, declarative_base,Session
from app.core.config import settings, get_ca_file

CA_PATH: pathlib.Path | None = get_ca_file()

connect_kwargs: dict[str, str] = {"sslmode": "verify-ca"}
if CA_PATH:
    connect_kwargs["sslrootcert"] = str(CA_PATH)

engine: Engine = create_engine(
    settings.DATABASE_URL,
    connect_args=connect_kwargs,
    pool_pre_ping=True,
)


SessionLocal: sessionmaker[Session] = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: Any = declarative_base()


# Dependency that routers use to get a DB session
def get_db() -> Generator[Session, Any, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()