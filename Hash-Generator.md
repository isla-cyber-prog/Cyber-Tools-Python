# Hash Generator

## Purpose

Generates SHA-256 hashes from user-provided text.

## Features

- SHA-256 Hashing
- User Input Processing
- Secure Hash Generation
- One-Way Hash Demonstration

## Skills Demonstrated

- Cryptography Fundamentals
- Python
- Hashing
- String handling
- Cybersecurity Concepts

## Example Code

```python
import hashlib

text = input("Enter text: ")

hash_value = hashlib.sha256(text.encode()).hexdigest()

print("SHA-256 Hash:")
print(hash_value)
```

## Example Output

```text
Enter text: password123

SHA-256 Hash:
ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

## Potential Applications

- Password Security
- Data Integrity Verification
- Digital Forensics
- Cybersecurity Education
