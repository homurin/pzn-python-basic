import utils.contact as contact

contact_list = [
    {
        "name": "fajrin",
        "email": "fajrin@gmail.com",
        "phoneNumber": "0881"
    },
    {
        "name": "fajri",
        "email": "fajrin@gmail.com",
        "phoneNumber": "0881"
    },
    {
        "name": "fajar",
        "email": "fajrin@gmail.com",
        "phoneNumber": "0881"
    },
]

while True:
    print("#menu")
    print("1. Contact List")
    print("2. New Contact")
    print("3. Delete Contact")
    print("4. Find Contact")
    print("0. Exit")

    menu = input("your choice: ")

    if (menu == "0"):
        break
    elif (menu == "1"):
        contact.find_all(contact_list)
    elif (menu == "2"):
        contact_list.append(contact.create_contact())
    elif (menu == "3"):
        contact.delete_contact(contact_list)
    elif (menu == "4"):
        contact.find_contact(contact_list)
    else:
        print("invalid menu input")
