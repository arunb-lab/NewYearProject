phonebook = {
    "Ram": "9800000000",
    "Sita": "9811111111",
    "Hari": "9822222222"
}

name = input("Search name: ")

if name in phonebook:
    print("Number:", phonebook[name])
else:
    print("Contact not found")
