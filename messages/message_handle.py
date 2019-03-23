class MessageHandle:
    def __init__(self, client_name, items=None, address=None):
        self.client_name = client_name
        self.items = items
        self.address = address

    @staticmethod
    def get_total_price(items):
        price = 0
        for item in items:
            price += item.get_total_price()
        return round(price, 2)

    @staticmethod
    def ask_for_address_msg():
        return "Qual o seu endereço?"

    @staticmethod
    def ask_for_client_name():
        return "Por favor, pode me dizer qual o seu nome?"

    @staticmethod
    def give_time_estimate(time):
        return f"Muito obrigado pelo pedido! Ele estará na sua casa em torno de {str(time)} minutos"

    def confirm_products_message(self):
        pass