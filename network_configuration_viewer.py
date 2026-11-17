import socket
import platform

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("IP Address:", ip)
print("Operating System:", platform.system())
