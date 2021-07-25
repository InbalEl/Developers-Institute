class Phone:
    def __init__(self, phone_number) -> None:
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def get_number(self):
        return self.phone_number

    def call(self, other_phone):
        new_call = f'{self.get_number()} called {other_phone.get_number()}'
        print(new_call)
        self.call_history.append(new_call)

    def send_message(self, other_phone, content):
        message = {'from': self.get_number(),
                   'to': other_phone.get_number(),
                   'content': content}
        
        print(message)
        self.messages.append(message)

    def show_outgoing_messages(self):
        for message in self.messages:
            if self.get_number() == message['from']:
                print(message)

    def show_incoming_messages(self):
        for message in self.messages:
            if self.get_number() != message['from']:
                print(message)

    def show_messages_from(self, other_phone):
        for message in self.messages:
            if other_phone.get_number() != message['from']:
                print(message)

    def show_call_history(self):
        for log in self.call_history:
            print(log)