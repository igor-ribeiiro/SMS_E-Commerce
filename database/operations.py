# -*- coding: utf-8 -*-
from database.models import User
from database.manager import SQLManager
from pprint import pprint


def get_users():
    session = SQLManager().get_session()
    response = session.query(User).all()
    session.close()
    return response


def add_user(name, phone, address):
    session = SQLManager().get_session()
    user = User(name, phone, address)
    session.add(user)
    session.commit()
    session.close()


if __name__ == '__main__':
    add_user("Igor Bragaia", "+55 19 97103-7086", "Rua H8A, apt 121")
    all_users = get_users()
    pprint(all_users)
