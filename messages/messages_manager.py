from messages.message_handle import MessageHandle
from messages.string_mathing import StringMathing
from messages.item import Item


class MessagesManager:
    def __init__(self, client_number, client_message):
        self.client_number = client_number
        self.client_message = client_message

    def get_message_to_be_sent(self):
        current_step = self.get_current_step()

        if current_step == 1:
            return self.parse_message_from_step_1()
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
        item3 = Item(name="refrigerante", qtd=6, price=3.5)
        stock = [item1, item2, item3]

        return stock

    def parse_message_from_step_1(self):
        client_items = self.client_message.split(",")
        stock = self.get_stock()
        string_mathing = StringMathing(stock)

        return_message = "\n"
        items = []
        total_price = 0

        for client_item in client_items:
            client_item = client_item.lstrip()
            # print(f"On client_item = {client_item}")
            item = client_item.split(" ")
            qtd = int(item[0])
            name = item[1]

            # print(f"Reading name = {name} and qtd = {qtd}")

            closest_item_from_stock = string_mathing.get_closest_item_from_string(name)
            # print(f"Closest from stock = {closest_item_from_stock.name}")
            # print("")

            items.append(closest_item_from_stock)

            price = qtd*closest_item_from_stock.price
            total_price += price
            price_str = f', preço = {price:.2f} confirmado,\n'
            return_message += f'{qtd} '+ closest_item_from_stock.name + price_str

        return_message = return_message[:-2]
        return_message += f'.\n\nPreço total = {total_price:.2f} reais\n'
        return_message += "Deixa separado ou entrega em casa?"
        return return_message

if __name__ == "__main__":
    message = "5 coca, 3 guarana, 7 refri"
    messages_manager = MessagesManager("my-number", message)
    messages_manager.get_message_to_be_sent()
