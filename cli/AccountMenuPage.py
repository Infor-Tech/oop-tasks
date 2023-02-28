class AccountMenuPage:
    def __init__(self, bank, client, account_id) -> None:
        self.BANK = bank
        self._client = client
        self._account = self.BANK.account_managment.authorise(client, account_id) # Req to banking system, get access to account
        if self._account == False:
            del(self)
            return 0
        self.run()

    def run(self):
        # Account Menu
        while True:
            print("------------------------")
            print(f"Account ID: {self._account.ACCOUNT_ID}\nCurrency: {self._account.CURRENCY}\nBalance: {self._account.get_balance()}")
            print("------------------------")
            print("1) Transfer funds\n2) Deposit\n3) History\n4) Close account\n5) Quit")
            action = int(input('Action: ')) 
            if action == 1: self.transfer_funds()
            elif action == 2: 
                # FOR TESTING ONLY, THIS IMPLEMENTATION BREAKS ALL ASSUMPTIONS
                amount = float(input("Deposit amount: "))
                self._account.receive(amount)
            elif action == 3: self.show_transactions()
            elif action == 4: self.close_account()
            elif action == 5: return 0
            else: print("Invalid choice")

    def transfer_funds(self):
        # User Input
        receiver_id = int(input("Receiver Account ID: "))
        title = input("Title: ")
        amount = float(input("Amount: "))

        # Req to banking system, try of making transfer
        response = self.BANK.account_managment.transfer_funds(self._account, receiver_id, title, amount)

        if response: print("Transfer successful")
        else: print("Something went wrong")

    def show_transactions(self):
        print("------------------------")
        print("TRANSACTION_ID | SENDER | RECEIVER | TITLE | AMOUNT | STATUS")
        transactions = self.BANK.transaction_keeping.get_account_transactions(self._account)
        for transaction in transactions:
            is_sender = transaction.SENDER_ACCOUNT == self._account
            if is_sender: amount = transaction.AMOUNT - 2*transaction.AMOUNT
            else: amount = transaction.AMOUNT
            print(f"{transaction.TRANSACTION_ID} | {transaction.SENDER_ACCOUNT.ACCOUNT_ID} | {transaction.RECEIVER.ACCOUNT_ID} | {transaction.TITLE} | {amount} | {transaction.get_status()}")


    def close_account(self):
        response = self.BANK.account_managment.close_account(self._account, self._client)
        if response: print("Account successfully closed")
        else: print("Something went wrong")
        del(self)
        return 0