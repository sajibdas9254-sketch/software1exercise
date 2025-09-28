# set the username and password to check later
cu = "python"
cp = "rules"
# set the value of i before entering the while loop
i = 1
while i <= 5:
    uname = input("Enter username: ")
    psw = input("Enter password: ")
    if (uname == cu) and (psw == cp):
        print("Welcome")
        break
    else:
        if (i >= 5):
            print("Access denied")
            break
        print("Incorrect username or password. Please try again.")
        i = i + 1