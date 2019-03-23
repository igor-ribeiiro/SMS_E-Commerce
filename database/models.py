# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode,  DateTime


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(), unique=True, nullable=False)
    address = Column(Unicode(), unique=False, nullable=False)
    phone = Column(Unicode(), unique=False, nullable=False)

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __repr__(self):
        return "name {0}, phone {1}, address {2}".format(self.name, self.phone, self.address)


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(), unique=True, nullable=False)
    qty = Column(Integer, unique=False, nullable=False)
    price = Column(Integer, unique=False, nullable=False)

    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def __repr__(self):
        return "name {0}, price {1}, qty {2}".format(self.name, self.qty, self.price)
