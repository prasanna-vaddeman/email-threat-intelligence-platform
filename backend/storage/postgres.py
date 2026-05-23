from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os


LOGGER = logging.getLogger(__name__)


DATABASE_URL = os.getenv(
    "DATABASE_URL"
)


engine = None
SessionLocal = None


if DATABASE_URL:

    try:

        engine = create_engine(

            DATABASE_URL,

            pool_pre_ping=True,

            pool_recycle=300

        )

        SessionLocal = sessionmaker(

            autocommit=False,

            autoflush=False,

            bind=engine

        )

        LOGGER.info(

            "Database connected"

        )

    except Exception as exc:

        LOGGER.exception(

            f"Database init failed: {exc}"

        )

else:

    LOGGER.warning(

        "DATABASE_URL missing. Storage disabled."

    )