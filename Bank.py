from Account import Account
from Client import Client
from Transaction import Transaction
from enums.Currency import Currency


class Bank:
    def __init__(self, name: str, address) -> None:
        self._name = name
        self._address = address
        self.account_managment = AccountManagement(self)
        self.client_managment = ClientManagement(self)
        self.transaction_keeping = TransactionKeeping()

    def get_info(self) -> dict:
        return {'name': self._name, 'address': self._address}


class AccountManagement:
    def __init__(self, bank: Bank) -> None:
        self.__client_accounts = {} # [client_id: int, list[Account]]
        self.__account_ownership = {} # [account_id: int, list[Client]]
        self.BANK = bank

    def open_account(self, client: Client, currency:Currency) -> Account:
        client_id = client[0].CLIENT_ID
        account = Account(currency, self.BANK)
        self.__account_ownership[account.ACCOUNT_ID] = [client[0]]
        try: self.__client_accounts[client_id].append(account)
        except KeyError: self.__client_accounts[client_id] = [account]
        return account.ACCOUNT_ID

    def close_account(self, account: Account, client_requesting: Client):
        clients = self.__account_ownership[account.ACCOUNT_ID]
        if client_requesting not in clients: return False
        for client in clients: self.__client_accounts[client[0].CLIENT_ID].remove(account)
        self.__account_ownership.pop(account.ACCOUNT_ID)
        del account
        return True
    
    def get_client_accounts(self, client) -> list:
        try: client_accounts = self.__client_accounts[client[0].CLIENT_ID]
        except KeyError: return []
        account_ids = []
        for account in client_accounts: account_ids.append(account.ACCOUNT_ID)
        return account_ids

    def authorise(self, client, requested_account_id):
        try: client_accounts = self.__client_accounts[client[0].CLIENT_ID]
        except KeyError: return False
        for account in client_accounts:
            if account.ACCOUNT_ID == requested_account_id: return account   
        return False

    def _get_account(self, account_id):
        try: owner = self.__account_ownership[account_id][0]
        except KeyError: return False

        owner_accounts = self.__client_accounts[owner.CLIENT_ID]
        for owner_account in owner_accounts:
            if owner_account.ACCOUNT_ID == account_id:
                account = owner_account
                break

        return account

    def transfer_funds(self, account, receiver_id, title, amount):
        receiver = self._get_account(receiver_id)
        transaction = Transaction(account, receiver, title, amount)
        self.BANK.transaction_keeping.add_transaction(transaction)
        result = transaction.commit()
        return result


class ClientManagement:
    def __init__(self, bank) -> None:
        self.BANK = bank
        self.__clients = {} #[int, [Client, password: str]]

    def add_client(self, name, last_name, password: str) -> int:
        client = Client(name, last_name, self.BANK)
        self.__clients[client.CLIENT_ID] = [client, password]
        return client.CLIENT_ID

    def authorise(self, client_id, given_password):
        try: client = self.__clients[client_id]
        except KeyError: return False
        if client[1] != given_password: return False
        return client


class TransactionKeeping:
    def __init__(self) -> None:
        self.__transactions = [] # [Transaction]
    def get_transactions(self):
        return self.__transactions
    def get_account_transactions(self, account: Account):
        transactions = []
        for transaction in self.__transactions:
            if transaction.SENDER_ACCOUNT == account or transaction.RECEIVER:
                transactions.append(transaction)
        return transactions
    def add_transaction(self, transaction):
        self.__transactions.append(transaction)