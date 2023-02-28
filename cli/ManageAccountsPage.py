from cli.AccountMenuPage import AccountMenuPage
from cli.authorise import authorise


class ManageAccountsPage:
    def __init__(self, bank) -> None:
        self.BANK = bank
        self._client = authorise(self.BANK)
        if self._client == False:
            del(self)
            return 0
        self.run()

    def run(self):
        print("Authentication successful, select your account: ")
        
        # Req to banking system, get list of client's accounts
        accounts = self.BANK.account_managment.get_client_accounts(self._client)
        
        # Account Choice Menu
        while True:
            i = 1
            for account_id in accounts:
                print(f"{i}) {account_id}")
                i += 1
            choice = int(input("Choice: "))
            try: account_id = accounts[choice - 1]
            except IndexError:
                print("Invalid choice, choose again")
                continue
            break

        AccountMenuPage(self.BANK, self._client, account_id)
