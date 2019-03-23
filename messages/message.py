class message:
    def __init__(self, client_name, items, address=None):
        self.client_name = client_name
        self.items = items
        self.address = address

    def get_total_price(self):
        price = 0
        for item in self.items:
            price += item.get_total_price()
        return price

    def confirm_products_message()
    