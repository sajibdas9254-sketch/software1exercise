c_name = "muath"
c_password = "muathbestteacher"
attempt = 0
max_attempt = 5
while attempt < max_attempt:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == c_name and password == c_password:
        print("Welcome!")
        break
    else:
        attempt += 1
        print(f"wrong credentials. Attempts left: {max_attempt - attempt}")
else:
    print("Access denied.")