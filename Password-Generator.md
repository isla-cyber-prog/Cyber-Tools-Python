# Password Generator

## Purpose

Generates secure random passwords to improve account security.

## Features

- Random Password Generation
- Adjustable Length
- Symbols
- Numbers
- Uppercase Letters
- Lowercase Letters

## Skills Demonstrated

- Python
- Randomisation
- Cybersecurity Awareness
- String Handling
- User Input

## Example Code

```python
import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)
```

## Example Output

```
Enter password length: 12

Generated Password:
T#8kL$2mP!9q
```
