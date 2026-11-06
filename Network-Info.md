# Network Information Tool

## Purpose

Displays basic network information about a device, including hostname and IP address.

## Features

- Hostname Lookup
- IP Address Lookup
- Basic Network Information
- Device Identification

## Skills Demonstrated

- Networking
- Python
- Hostname Resolution
- IP Addressing
- System Information Retrieval

## Example Code

```python
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("IP Address:", ip_address)
```

## Example Output

```text
Hostname: Example-PC
IP Address: 192.168.1.100
```
