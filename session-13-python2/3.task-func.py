# write a function which takes 2 parameters username and password and prints
#if username is admin and password is admin123 then print login success
#else print login failed

def login(username, password):
    if username == "admin" and password == "admin123":
        print("login success")
    else:
        print("login failed")

username = input("Enter username: ")
password = input("Enter password: ")

login(username, password)
