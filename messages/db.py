from database.operations import get_items, add_user, update_address, update_name
from pprint import pprint


class DB:
    def __init__(self, client_number, client_message):
        self.client_number = client_number
        self.client_message = client_message

    def get_stock(self):
        return get_items()

    def get_current_step(self): #para dado phone
        return 4

    def remove_product_from_db(self, id, qty): #nome, qty
        pass

    def update_address(self, phone, address): #phone, address
        update_address(phone, address)

    def update_name(self, phone, name): #phone, name
        update_name(phone, name)

    def create_user(self, phone):
        add_user("", phone, "")

    def get_time_estimative(self):
        return 45


if __name__ == '__main__':
    print("Querying items")
    all_items = get_items()
    pprint(all_items)
