# Log File Analyser

## Purpose

Analyses log files to identify suspicious activity and security related events.

## Features

- Count Failed Login Attempts
- Detect Frequent IP Addresses
- Generate Summary Reports
- Identify Suspicious Activity

## Skills Demonstrated

- Python
- Log Analysis
- Security Monitoring
- File Handling
- Data processing
- Cybersecurity Concepts

  ## Example Code

```python
filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        log = file.read()

    failed_logins = log.upper().count("FAILED")

    print("Failed Login Attempts:", failed_logins)

except FileNotFoundError:
    print("Log file not found.")
```

## Example Output

```text
Enter log file name: access.log

Failed Login Attempts: 12
```

## Potential Applications

- Security Monitoring
- Incident Investigation
- Threat Detection
- System Administration
