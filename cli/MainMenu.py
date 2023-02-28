from cli.CreateAccountPage import CreateAccountPage
from cli.CreateClientPage import CreateClientPage
from cli.ManageAccountsPage import ManageAccountsPage


class MainMenu:
    def __init__(self, bank) -> None:
        self.BANK = bank
        self.run()

    def run(self):
        bank_info = self.BANK.get_info()
        while True:
            print(f"Welcome in {bank_info['name']}\nSelect action")
            print("1) Become a client\n2) Create an account\n3) Manage Accounts\n4) Quit")
            action = int(input('Action: ')) 

            if action == 1: CreateClientPage(self.BANK)
            elif action == 2: CreateAccountPage(self.BANK)
            elif action == 3: ManageAccountsPage(self.BANK)
            elif action == 4: return 0
            else: print("Invalid choice")