# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode,  DateTime


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(), unique=False, nullable=False)
    address = Column(Unicode(), unique=False, nullable=False)
    phone = Column(Unicode(), unique=False, nullable=False)

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __repr__(self):
        return "name {0}, phone {1}, address {2}".format(self.name, self.phone, self.address)

