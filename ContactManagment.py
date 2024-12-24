def addContact():
    name = input("Enter the name: ")
    phone = input("Enter the phone: ")
    email = input("Enter the email: ")

    with open("contacts.txt", "a") as file:
        if "@" not in email or "." not in email:
            print("Invalid Email")
        else:
            file.write(name + " " + phone + " " + email + "\n")
            print("Contact Added Successfully")


def editContact():
    name = input("Enter the name of the contact you want to edit: ")
    new_phone = input("Enter the new phone (leave blank to skip): ")
    if new_phone == "":
        new_phone = None

    new_email = input("Enter the new email (leave blank to skip): ")
    if new_email == "":
        new_email = None

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    with open("contacts.txt", "w") as file:
        contact_found = False
        for contact in contacts:
            contact_details = contact.strip().split(" ")
            if contact_details[0] == name:
                contact_found = True
                if new_phone:
                    contact_details[1] = new_phone
                if new_email:
                    contact_details[2] = new_email

                file.write(" ".join(contact_details) + "\n")
            else:
                file.write(contact)

        if contact_found:
            print("Contact updated successfully.")
        else:
            print("Contact not found.")


def showContacts():
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()
    for contact in contacts:
        print(contact.strip())


def deleteContact():
    name = input("Enter the name of the contact you want to delete: ")
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    with open("contacts.txt", "w") as file:
        contact_found = False
        for contact in contacts:
            contact_details = contact.strip().split(" ")
            if contact_details[0] == name:
                contact_found = True
                print(f"Contact {name} deleted successfully.")
                continue
            else:
                file.write(contact)

        if not contact_found:
            print(f"Contact {name} not found.")


def searchContact():
    name = input("Enter the name you want to search: ")
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    contact_found = False
    for contact in contacts:
        contact_details = contact.strip().split(" ")
        if contact_details[0] == name:
            print(contact_details)
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
