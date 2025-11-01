password = input()
def valid_password(password):
    is_valid = True
    if len(password) > 10 or len(password) < 6:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    digits_count = sum(char.isdigit() for char in password)
    if digits_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")
valid_password(password)