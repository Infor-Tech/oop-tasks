from Person import Person


class Client(Person):
    count = 0
    def __init__(self, name, last_name, bank) -> None:
        super().__init__(name, last_name)
        Client.count += 1
        self.CLIENT_ID = Client.count
        self.BANK = bank