from Account import Account
from enums.TransactionStatus import TransactionStatus


class Transaction:
    count = 0
    def __init__(self, sender_account: Account, receiver: Account, title, amount: float) -> None:
        Transaction.count += 1
        self.TRANSACTION_ID = Transaction.count
        self.SENDER_ACCOUNT = sender_account
        self.RECEIVER = receiver
        self.TITLE = title
        self.AMOUNT = amount
        self._transaction_status = TransactionStatus['ORDERED']

    def _transfer(self):
        if self.SENDER_ACCOUNT.CURRENCY != self.RECEIVER.CURRENCY: return False
        result = self.SENDER_ACCOUNT.withdraw(self.AMOUNT)
        if not result: return False
        self.RECEIVER.receive(self.AMOUNT)
        return True

    def get_status(self):
        return self.transaction_status

    def commit(self):
        self.transaction_status = TransactionStatus['PROCESSED']
        if self._transfer():
            self.transaction_status = TransactionStatus['COMPLETED']
            return True
        self.transaction_status = TransactionStatus['FAILED']
        return False
