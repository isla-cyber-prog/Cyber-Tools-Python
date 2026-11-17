import hashlib

def get_hash(filename):
    with open(filename, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()

original = input("Enter original file: ")
backup = input("Enter backup file: ")

if get_hash(original) == get_hash(backup):
    print("Backup verified. Files match.")
else:
    print("Warning: Files differ.")
