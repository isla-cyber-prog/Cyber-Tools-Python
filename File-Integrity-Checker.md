# File Integrity Checker

## Purpose

Checks whether a file has been modified by comparing its hash value.

## Features

- Generate Hash
- Verify Hash
- File Monitoring

## Skills Demonstrated

- Python 
- File Handling
- Hashing
- Integrity Verification

## Example Code

```python
import hashlib

filename = input("Enter file name: ")

with open(filename, "rb") as file:
    data = file.read()

hash_value = hashlib.sha256(data).hexdigest()

print("File Hash:")
print(hash_value)
```
## Example output:

```text
Enter file name: document.txt

File Hash:
f2ca1bb6c7e907d06dafe4687e579fce9f1f0e4d1e5f3a4d7f6c8a9b0c1d2e3f
```
