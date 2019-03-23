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


def add_kart(phone, price, order):
    session = SQLManager().get_session()

    user = session.query(User).filter_by(phone=phone).first()

    kart = Kart(user.id, order, price)
    session.add(kart)

    user.karts.append(kart)

    session.commit()
    session.close()


def close_kart(phone):
    session = SQLManager().get_session()

    user = session.query(User).filter_by(phone=phone).first()

    last_kart = session.query(Kart).filter_by(user_id=user.id, finished=0).order_by('date').first()
    last_kart.finished = 1

    session.commit()
    session.close()


def update_buscar_na_loja(phone, buscar_na_loja):
    session = SQLManager().get_session()

    user = session.query(User).filter_by(phone=phone).first()

    last_kart = session.query(Kart).filter_by(user_id=user.id, finished=0).order_by('date').first()
    last_kart.buscar_na_loja = buscar_na_loja

    session.commit()
    session.close()


def get_buscar_na_loja(phone):
    session = SQLManager().get_session()

    user = session.query(User).filter_by(phone=phone).first()

    last_kart = session.query(Kart).filter_by(user_id=user.id, finished=0).order_by('date').first()
    buscar_na_loja = last_kart.buscar_na_loja

    session.commit()
    session.close()

    return buscar_na_loja


def update_step(phone):
    session = SQLManager().get_session()

    user = session.query(User).filter_by(phone=phone).first()

    last_kart = session.query(Kart).filter_by(user_id=user.id, finished=0).order_by('date').first()
    current_step = int(last_kart.step)
    last_kart.step += 1

    session.commit()
    session.close()

    return current_step


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
    phone = "01012093"
    add_user("Igor Bragaia", "Rua H8A, apt 121", phone)
    all_users = get_users()
    pprint(all_users)

    # update_name(phone, "aha")
    # all_users = get_users()
    # pprint(all_users)
    #
    # update_address(phone, "av bagulho eh loko")
    # all_users = get_users()
    # pprint(all_users)

    print("Adding kart to user")
    add_kart(phone, 123, ["2 unit item cartas", "3 unit item z"])
    all_users = get_users()
    pprint(all_users)

    step = update_step(phone)
    all_users = get_users()
    pprint(all_users)

    update_step(phone)
    all_users = get_users()
    pprint(all_users)

    update_step(phone)
    all_users = get_users()
    pprint(all_users)

    update_step(phone)
    all_users = get_users()
    pprint(all_users)

    update_buscar_na_loja(phone, 1)
    all_users = get_users()
    pprint(all_users)

    close_kart(phone)
    all_users = get_users()
    pprint(all_users)

    # print("Querying items")
    # add_item("random1", 50, 9)
    # all_items = get_items()
    # pprint(all_items)
    # delete_item("random1", 3)
    # all_items = get_items()
    # print(all_items)
    # items = [item.as_dict() for item in all_items]
    # print(items)
