# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode,  DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(), unique=False, nullable=False)
    address = Column(Unicode(), unique=False, nullable=False)
    phone = Column(Unicode(), unique=True, nullable=False)
    karts = relationship('Kart', lazy='subquery', backref='user')

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.karts = []

    def __repr__(self):
        return "name {0}, phone {1}, address {2}, karts {3}".format(self.name, self.phone, self.address, self.karts)

    def as_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "address": self.address,
            "karts": [kart.as_dict() for kart in self.karts]
        }


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(), unique=True, nullable=False)
    qty = Column(Integer, unique=False, nullable=False)
    price = Column(Integer, unique=False, nullable=False)

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def __repr__(self):
        return "name {0}, price {1}, qty {2}".format(self.name, self.price, self.qty)


class Kart(Base):
    __tablename__ = "kart"
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(), unique=False, nullable=False)
    order = Column(ARRAY(Unicode()), unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, name, user_id, order):
        self.name = name
        self.user_id = user_id
        self.order = order

    def __repr__(self):
        return "customer {0}, kart {1}".format(self.user_id, self.name)

    def as_dict(self):
        return {
            "kart": self.name,
            "order": self.order
        }
