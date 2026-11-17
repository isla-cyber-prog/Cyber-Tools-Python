filename = input("Enter log file: ")

info = 0
warning = 0
error = 0

with open(filename, "r") as file:
    for line in file:
        if "INFO" in line:
            info += 1
        elif "WARNING" in line:
            warning += 1
        elif "ERROR" in line:
            error += 1

print("\nLog Summary")
print("INFO:", info)
print("WARNING:", warning)
print("ERROR:", error)
