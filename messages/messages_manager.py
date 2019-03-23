from message_handle import MessageHandle
from string_mathing import StringMathing
from item import Item


class MessagesManager:
    def __init__(self, client_number, client_message):
        self.client_number = client_number
        self.client_message = client_message

    def get_message_to_be_sent(self):
        current_step = self.get_current_step()
        print(f"On step = {current_step}.")
        print(f"Client_number = {self.client_number} and client_message = {self.client_message}")
        print("")

        if current_step == 1:
            self.parse_message_from_step_1()
            return "Nothing"
        elif current_step == 2:
            return MessageHandle.ask_for_address_msg()
        elif current_step == 3:
            return MessageHandle.ask_for_client_name()
        elif current_step == 4:
            return MessageHandle.give_time_estimate(self.client_message)
        else:
            print(f"Error: receive current_step = {current_step} not between 1 and 4")

    def get_current_step(self):
        return 1

    def get_stock(self):
        item1 = Item(name="coca-cola", qtd=4, price=4)
        item2 = Item(name="guarana", qtd=3, price=5)
        item3 = Item(name="refri", qtd=6, price=3.5)
        stock = [item1, item2, item3]

        return stock

    def parse_message_from_step_1(self):
        client_items = self.client_message.split(",")
        stock = self.get_stock()
        string_mathing = StringMathing(stock)

        for client_item in client_items:
            client_item = client_item.lstrip()
            print(f"On client_item = {client_item}")
            item = client_item.split(" ")
            qtd = item[0]
            name = item[1]

            print(f"Reading name = {name} and qtd = {qtd}")

            closest_from_stock = string_mathing.get_closest_item_from_string(name)
            print(f"Closest from stock = {closest_from_stock.name}")
            print("")


if __name__ == "__main__":
    message = "5 coca, 3 guarana, 7 refrigerante"
    messages_manager = MessagesManager("my-number", message)
    messages_manager.get_message_to_be_sent()

