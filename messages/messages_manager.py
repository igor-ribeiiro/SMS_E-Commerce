from message_handle import MessageHandle


class MessagesManager:
    def __init__(self, client_number, client_message):
        self.client_number = client_number
        self.client_message = client_message
        self.message_handle = MessageHandle()

    def get_message_to_be_sent(self):
        current_step = self.get_current_step()
        print(f"On step = {current_step}. Client_number = {self.client_number} and client_message = {self.client_message}")

        if current_step == 1:
            pass
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