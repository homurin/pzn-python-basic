def find_all(contacts):
    if (len(contacts) == 0):
        print("empty contact")
    for contact in contacts:
        print("============")
        print(f"name: {contact['name']}")
        print(f"email: {contact['email']}")
        print(f"phone number: {contact['phoneNumber']}")


def find_contact(contacts):
    name = input("input contact name: ")

    for contact in contacts:
        if (contact["name"].lower().find(name.lower()) != -1):
            print("============")
            print(f"name: {contact['name']}")
            print(f"email: {contact['email']}")
            print(f"phone number: {contact['phoneNumber']}")
        else:
            print("contact not found")


def create_contact():
    name = input("input your name: ")
    email = input("input your email: ")
    phone_number = input("input your phone number: ")

    contact = {
        "name": name,
        "email": email,
        "phoneNumber": phone_number
    }
    return contact


def delete_contact(contacts):
    phone_number = input("phone number to delete: ")

    for i in range(0, len(contacts)):
        contact = contacts[i]
        if (contact["phoneNumber"] == phone_number):
            del contacts[i]
            print(f"delete contact success")
            break
        else:
            print("contact not found")
