class Item:
    def __init__(self, name, qty, price, id=None):
        self.name =name
        self.qty = qty
        self.price = price
        self.id = id

    def get_total_price(self):
        return self.price*self.qty
