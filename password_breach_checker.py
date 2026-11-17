common_passwords = [
    "password",
    "123456",
    "password123",
    "qwerty",
    "letmein"
]

password = input("Enter password: ")

if password.lower() in common_passwords:
    print("Warning: Password found in weak password database.")
else:
    print("Password not found in database.")
