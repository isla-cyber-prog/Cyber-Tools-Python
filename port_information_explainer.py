ports = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

port = int(input("Enter port number: "))

if port in ports:
    print("Service:", ports[port])
else:
    print("Port not in database.")
