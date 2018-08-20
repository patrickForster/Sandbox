MIN_LENGTH = 4
print("Please enter a valid password")
print("Your password must be at least", MIN_LENGTH, "characters long")
password = input("> ")
while len(password) < MIN_LENGTH:
    print("Not enough characters!")
    password = input("> ")
hidden_password = len(password)*'*'
print("Your {}-character password is valid: {}".format(len(password), hidden_password))
