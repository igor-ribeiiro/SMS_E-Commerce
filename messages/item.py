class Item:
    def __init__(self, name, qtd, price, id=None):
        self.name =name
        self.qtd = qtd
        self.price = price
        self.id = id

    def get_total_price(self):
        return self.price*self.qtd
