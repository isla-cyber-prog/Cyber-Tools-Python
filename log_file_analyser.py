filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        log = file.read()

    failed_logins = log.upper().count("FAILED")

    print("Failed Login Attempts:", failed_logins)

except FileNotFoundError:
    print("Log file not found.")
