from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_URL is None:

    raise ValueError(

        "DATABASE_URL environment variable missing"

    )


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