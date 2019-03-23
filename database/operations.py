# -*- coding: utf-8 -*-
from database.models import User, Item, Kart
from database.manager import SQLManager
from pprint import pprint


def get_user(phone):
    session = SQLManager().get_session()
    user = session.query(User).filter_by(phone=phone).first()
    session.close()
    return user

def get_users():
    session = SQLManager().get_session()
    users = session.query(User).all()
    session.close()
    return [user.as_dict() for user in users]


def add_user(name, phone, address):
    session = SQLManager().get_session()
    user = User(name, phone, address)
    session.add(user)
    session.commit()
    session.close()


def update_name(phone, name):
    session = SQLManager().get_session()
    user = session.query(User).filter_by(phone=phone).first()
    user.name = name
    session.commit()
    session.close()


def update_address(phone, address):
    session = SQLManager().get_session()
    user = session.query(User).filter_by(phone=phone).first()
    user.address = address
    session.commit()
    session.close()


def add_kart(phone, name, order):
    session = SQLManager().get_session()

    user = session.query(User).filter_by(address=phone).first()

    kart = Kart(name, user.id, order)
    session.add(kart)

    user.karts.append(kart)

    session.commit()
    session.close()


def get_items():
    session = SQLManager().get_session()
    response = session.query(Item).all()
    session.close()
    return response


def delete_item(name, qty):
    session = SQLManager().get_session()
    response = session.query(Item).filter_by(name=name).first()
    response.qty = max(0, response.qty - qty)
    session.commit()
    session.close()


def add_item(name, price, qty):
    session = SQLManager().get_session()
    item = Item(name, price, qty)
    session.add(item)
    session.commit()
    session.close()


if __name__ == '__main__':
    # print("Querying users")
    # phone = "01012093"
    # # add_user("Igor Bragaia", "Rua H8A, apt 121", phone)
    # all_users = get_users()
    # pprint(all_users)
    #
    # update_name(phone, "aha")
    # all_users = get_users()
    # pprint(all_users)
    #
    # update_address(phone, "av bagulho eh loko")
    # all_users = get_users()
    # pprint(all_users)

    # print("Adding kart to user")
    # add_kart("+55 19 97103-7086", "kart dono", ["2 unit item cartas", "3 unit item z"])

    print("Querying items")
    # add_item("random123", 50, 9)
    # all_items = get_items()
    # pprint(all_items)
    # delete_item("random123", 3)
    all_items = get_items()
    print(all_items)
    items = [item.as_dict() for item in all_items]
    print(items)
