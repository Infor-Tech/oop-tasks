class CreateClientPage:
    def __init__(self, bank) -> None:
        self.BANK = bank
        self.run()

    def run(self):
        # Client creation form
        print("------------------------\nInsert your personal info below")
        name = str(input("Name: "))
        last_name = str(input("Last name: "))
        password = str(input("Password: "))

        # Req to banking system, create account in banking system
        account_id = self.BANK.client_managment.add_client(name, last_name, password)
        print(f"Account created, your id is: {account_id}")