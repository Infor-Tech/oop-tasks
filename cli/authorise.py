def authorise(bank):
    print("------------------------\nAuthorise")
    client_id = int(input("Client ID: "))
    password = str(input("Password: "))
    client = bank.client_managment.authorise(client_id, password)
    return client
