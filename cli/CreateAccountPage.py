from cli.authorise import authorise
from enums.Currency import Currency


class CreateAccountPage:
    def __init__(self, bank) -> None:
        self.BANK = bank
        self._client = authorise(self.BANK)
        if self._client == False:
            del(self)
            return 0
        self.run()

    def run(self):
        print("Authentication successful, select currency: ")

        # Currency choice
        while True:
            i = 1
            for value in Currency:
                print(f"{i}) {value}")
                i += 1
            currency = int(input("Choice: "))
            if currency <= len(Currency):
                break
            print("Invalid choice, choose again")
        
        # Req to banking system
        account_id = self.BANK.account_managment.open_account(self._client, Currency(currency))
        print(f"Account creation successful, account id: {account_id}")
