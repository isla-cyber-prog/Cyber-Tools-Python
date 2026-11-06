import hashlib

filename = input("Enter file name: ")

with open(filename, "rb") as file:
    data = file.read()

hash_value = hashlib.sha256(data).hexdigest()

print("File Hash:")
print(hash_value)
