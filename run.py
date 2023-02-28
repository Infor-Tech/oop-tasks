from Bank import Bank
from cli.MainMenu import MainMenu

'''
Execute this file
'''

def main():
    bank = Bank("Bank", "Bank")
    MainMenu(bank)

if __name__ == '__main__':
    main()