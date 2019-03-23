from messages.item import Item


class DB:
    def __init__(self, client_number, client_message):
        self.client_number = client_number
        self.client_message = client_message

    def get_stock(self):
        item1 = Item(name="coca-cola", qtd=4, price=4)
        item2 = Item(name="guarana", qtd=3, price=5)
        item3 = Item(name="refrigerante", qtd=6, price=3.5)
        stock = [item1, item2, item3]

        return stock

    def get_current_step(self):
        return 1

    def remove_product_from_db(self, id, qtd):
        pass

    def save_address(self, address):
        pass

    def save_client_name(self, name):
        pass
