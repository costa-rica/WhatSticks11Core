# # print("- in ws_models/Base")

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from .config import config
from contextlib import contextmanager

Base = declarative_base()
engine = create_engine(config.SQL_URI_WHAT_STICKS_DB)
Session = sessionmaker(bind = engine)
# sess = Session()

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()