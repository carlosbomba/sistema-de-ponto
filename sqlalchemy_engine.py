import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SqlAlchemyDbEngine:
    def __init__(self):
        self.alchemy_engine_url = os.getenv("ALCHEMY_ENGINE_URL")
        self.engine = self.__create_engine()
        self.session = None

    def __create_engine(self):
        engine = create_engine(self.alchemy_engine_url)
        return engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.engine)
        self.session = session_make()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
