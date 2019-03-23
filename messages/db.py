from database.operations import get_items, add_user, update_address, update_name, delete_item, get_user, add_kart, update_step, \
    update_buscar_na_loja, get_buscar_na_loja, close_kart
from pprint import pprint


class DB:
    def __init__(self, client_number, client_message):
        self.client_number = client_number
        self.client_message = client_message

    def get_stock(self):
        return get_items()

    def close_kart(self, phone):
        close_kart(phone)

    def get_current_step(self, phone): # para dado phone
        try:
            return update_step(phone)
        except:
            return 1

    def save_carrinho(self, phone, items, price): #items = ["string1", "string2", "string2"]
        print(f"phone = {phone}")
        add_kart(phone, price, items)

    def remove_product_from_db(self, name, qty): #nome, qty
        delete_item(name, qty)

    def update_address(self, phone, address): #phone, address
        update_address(phone, address)

    def update_name(self, phone, name): #phone, name
        update_name(phone, name)

    def create_user(self, phone):
        print(f"Phone = {phone} no create_user")
        add_user("", phone, "")

    def update_para_buscar_na_loja(self, phone, vai_buscar_na_loja): # 0 ou 1
        update_buscar_na_loja(phone, vai_buscar_na_loja)

    def get_para_buscar_na_loja(self, phone): # 0 ou 1
        return not get_buscar_na_loja(phone)

    def get_client_name(self, phone):
        return get_user(phone).name

    def get_client_address(self, phone):
        return get_user(phone).address

    def get_time_estimative(self):
        return 45

    def get_comerciante_phone_numer(self):
        return '+5585999911065'


if __name__ == '__main__':
    print("Querying items")
    all_items = get_items()
    pprint(all_items)
