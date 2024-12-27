import json

def loadContacts():
    try:
        with open("contacts.json" , "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def saveContacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)



def addContact():
    name = input("Enter the name: ")
    phone = input("Enter the phone: ")
    email = input("Enter the email: ")

    if "@" not in email or "." not in email:
        print("Invalid email address.")
        return

    contacts = loadContacts()

    for contact in contacts:
        if contact["name"] == name:
            print("Contact with this name already exists.")
            return
    new_contact = {"name": name,
                   "phone": phone,
                   "email": email}
    contacts.append(new_contact)
    saveContacts(contacts)
    print("Contact added successfully.")


def editContact():
    name = input("Enter the name of the contact you want to edit: ")
    new_phone = input("Enter the new phone (leave blank to skip): ")
    new_email = input("Enter the new email (leave blank to skip): ")

    contacts = loadContacts()
    contactFound = False

    for contact in contacts:
        if contact["name"] == name:
            contactFound = True
            if new_phone:
                contact["phone"] = new_phone
                print("Phone updated successfully.")
            if new_email:
                contact["email"] = new_email
                print("Email updated successfully.")
            saveContacts(contacts)
            break
    if not contactFound:
            print("Contact not found.")


def showContacts():
    contacts = loadContacts()
    for contact in contacts:
        print(contact)


def deleteContact():
    name = input("Enter the name of the contact you want to delete: ")
    contacts = loadContacts()
    contactFound = False

    for contact in contacts :
        if contact["name"] == name:
            contacts.remove(contact)
            saveContacts(contacts)
            print("Contact deleted successfully.")
            contactFound = True
            break

    if not contactFound :
        print("Contact not found.")


def searchContact():
    name = input("Enter the name you want to search: ")
    contacts = loadContacts()
    contact_found = False

    for contact in contacts:
        if contact["name"] == name:
            print(contact)
            contact_found = True
            break
    if not contact_found:
        print("Contact not found.")


def main():
    while True:
        print("\n------Welcome to Contact Management System------")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Show Contacts")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            addContact()
        elif choice == "2":
            editContact()
        elif choice == "3":
            showContacts()
        elif choice == "4":
            deleteContact()
        elif choice == "5":
            searchContact()
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Invalid option, please try again.")


# Start the program
if __name__ == "__main__":
    main()
