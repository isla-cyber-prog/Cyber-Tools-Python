import hashlib

def file_hash(filename):
    with open(filename, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()

file1 = input("Enter first file: ")
file2 = input("Enter second file: ")

if file_hash(file1) == file_hash(file2):
    print("Files match.")
else:
    print("Files do not match.")
