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

    def ask_for_address_msg(self):
        return "Qual o seu endereço?"

    def ask_for_client_name(self):
        return "Por favor, pode me dizer qual o seu nome?"

    def give_time_estimate(self, time):
        return f"Muito obrigado pelo pedido! Ele estará na sua casa em torno de {str(time)} minutos"

    def confirm_products_message():
        pass