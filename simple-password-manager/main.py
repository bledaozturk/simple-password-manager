passwords = {}

while True:
    service = input("Type in the service (or press Enter to stop): ")
    if service == "":
        break

    password = input(f"Type in the password for {service}: ")
    if password == "":
        break

    passwords[service] = password

print("\nSaved passwords:")
for service, password in passwords.items():
    print(f"{service}: {password}")
    

