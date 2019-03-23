# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
import os


class SQLManager:
    def __init__(self):
        self.url = url = os.environ.get('DATABASE_URL')
        self.engine = create_engine(url)

    def create_all_tables(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        Base.metadata.bind = self.engine
        db_session = sessionmaker(bind=self.engine)
        session = db_session()
        return session

    def deleteAll(self):
        Base.metadata.drop_all(self.engine)


if __name__ == '__main__':
    sqlmanager = SQLManager()
    sqlmanager.deleteAll()
    sqlmanager.create_all_tables()
