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

with open(filename, "r") as file:
    log = file.read()

failed_logins = log.count("FAILED LOGIN")

print("Failed Login Attempts:", failed_logins)
```

## Example Output

```text
Enter log file name: access.log

Failed Login Attempts: 3
```

## Potential Applications

- Security Monitoring
- Incident Investigation
- Threat Detection
- System Administration
