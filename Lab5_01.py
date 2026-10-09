username = "admin"
password = "1234"

username = input("Enter your username : ")
password = input("Enter your password : ")
print("\n========== LOGIN RESULT ==========\n")

if username == "admin" and password == "1234":
    print("\nLogin Complete\n")
    print(f"Username : {username}")
    print(f"Password : {password}")
else:
    print("Login failed - Invalid username or password")