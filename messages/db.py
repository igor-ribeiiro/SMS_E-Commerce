from messages.item import Item
from database.operations import get_items
from pprint import pprint

class DB:
    def __init__(self, client_number, client_message):
        self.client_number = client_number
        self.client_message = client_message

    def get_stock(self):
        return get_items()

    def get_current_step(self): #para dado phone
        return 1

    def remove_product_from_db(self, id, qtd): #nome, qtd
        pass

    def save_address(self, address): #phone, address
        pass

    def save_client_name(self, name): #phone, name
        pass

if __name__ == '__main__':
    print("Querying items")
    all_items = get_items()
    pprint(all_items)
