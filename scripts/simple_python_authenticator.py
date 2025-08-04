def login(username, password):
    if username == "admin" and password == "0000":
        return True
    else:
        return False

for i in range(3):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if login(username, password):
        print("Access Granted")
        break
    else:
        attempts_left = 2 - i
        if attempts_left > 0:
            print(f"Access Denied. You have {attempts_left} attempt(s) left.\n")
        else:
            print("❌ Access Denied. No attempts left.")
            print("🔒 Account locked.")
