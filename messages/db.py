from database.operations import get_items, add_user, update_address, update_name, delete_item
from pprint import pprint


class DB:
    def __init__(self, client_number, client_message):
        self.client_number = client_number
        self.client_message = client_message

    def get_stock(self):
        return get_items()

    def get_current_step(self): #para dado phone
        return 4

    def save_carrinho(self, items):
        pass

    def remove_product_from_db(self, name, qty): #nome, qty
        delete_item(name, qty)

    def update_address(self, phone, address): #phone, address
        update_address(phone, address)

    def update_name(self, phone, name): #phone, name
        update_name(phone, name)

    def create_user(self, phone):
        add_user("", phone, "")
    def get_address(self): #phone, address
        return "Meu endereço"

    def save_client_name(self, name): #phone, name
        pass

    def get_para_buscar_na_loja(self): # Retorna True ou False
        return True

    def get_client_name(self):
        return "Igor"

    def get_time_estimative(self):
        return 45

    def get_comerciante_phone_numer(self):
        return '+5585999911065'


if __name__ == '__main__':
    print("Querying items")
    all_items = get_items()
    pprint(all_items)
