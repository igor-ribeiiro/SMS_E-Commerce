from messages.message_handle import MessageHandle
from messages.string_mathing import StringMathing
from messages.db import DB
from messages.sms import SMS

sms = SMS()

class MessagesManager:
    def __init__(self, client_number, client_message):
        self.client_number = client_number
        self.client_message = client_message
        self.db = DB(client_number, client_message)

    def get_message_to_be_sent(self):
        current_step = self.db.get_current_step(self.client_number)

        if current_step == 1:
            self.db.create_user(self.client_number)
            return self.parse_message_from_step_1()
        elif current_step == 2:
            buscar_na_loja = False
            if StringMathing.similar(self.client_message, "loja") >= 0.5 or \
                StringMathing.similar(self.client_message, "Pegar na loja") >= 0.5:
                buscar_na_loja = True

            self.db.update_para_buscar_na_loja(self.client_number, buscar_na_loja)
            return MessageHandle.ask_for_address_msg()
        elif current_step == 3:
            self.db.update_address(self.client_number, self.client_message)

            return MessageHandle.ask_for_client_name()
        elif current_step == 4:
            self.db.update_name(self.client_number, self.client_message)

            sms.send_sms(self.db.get_comerciante_phone_numer(), self.get_message_to_comerciante_4())

            self.db.close_kart(self.client_number)
            if self.db.get_para_buscar_na_loja(self.client_number):
                return MessageHandle.say_your_pedido_is_ready()
            else:
                return MessageHandle.give_time_estimate(self.db.get_time_estimative())
        else:
            print(f"Error: receive current_step = {current_step} not between 1 and 4")

    def get_message_to_comerciante_4(self):
        client_name = self.db.get_client_name(self.client_number)
        message = f"Compra realizada pelo cliente {client_name}.\n"
        if self.db.get_para_buscar_na_loja(self.client_number):
            message += "Cliente irá buscar na loja.\n"
        else:
            message += "Pedido para entregar no endereço: " + self.db.get_client_address(self.client_number) + ".\n"
        message += "Favor, consultar plataforma virtual para ver os produtos pedidos."
        return message

    def parse_message_from_step_1(self):
        client_items = self.client_message.split(",")
        stock = self.db.get_stock()
        string_mathing = StringMathing(stock)

        return_message = "\n"
        items = []
        items_str = []
        total_price = 0

        for client_item in client_items:
            client_item = client_item.lstrip()
            item = client_item.split(" ")
            qty = int(item[0])
            name = item[1]

            closest_item_from_stock = string_mathing.get_closest_item_from_string(name)
            items.append(closest_item_from_stock)

            if qty == 1:
                items_str.append(str(qty) + " unidade de " + closest_item_from_stock.name)
            else:
                items_str.append(str(qty) + " unidades de " + closest_item_from_stock.name)

            price = qty*closest_item_from_stock.price
            total_price += price
            price_str = f', preço = {price:.2f} confirmado,\n'
            return_message += f'{qty} '+ closest_item_from_stock.name + price_str

            self.db.remove_product_from_db(closest_item_from_stock.name, qty)

        print(f"PHONE = {self.client_number}")
        self.db.save_carrinho(self.client_number, items_str, total_price)
        return_message = return_message[:-2]
        return_message += f'.\n\nPreço total = {total_price:.2f} reais\n'
        return_message += "Pegar na loja ou entrega em casa?"
        return return_message


if __name__ == "__main__":
    message = "5 coca, 3 guarana, 7 refri"
    messages_manager = MessagesManager("my-number", message)
    messages_manager.get_message_to_be_sent()
