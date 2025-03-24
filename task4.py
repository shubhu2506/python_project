import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts = load_contacts()
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"{name} - {details['Phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ").strip()
    contacts = load_contacts()
    for name, details in contacts.items():
        if search in [name, details["Phone"]]:
            print(f"\nFound Contact:\nName: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    contacts = load_contacts()
    if name not in contacts:
        print("Contact not found.")
        return
    
    print("Enter new details (leave blank to keep existing values):")
    phone = input(f"New phone ({contacts[name]['Phone']}): ").strip() or contacts[name]["Phone"]
    email = input(f"New email ({contacts[name]['Email']}): ").strip() or contacts[name]["Email"]
    address = input(f"New address ({contacts[name]['Address']}): ").strip() or contacts[name]["Address"]

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()



#output
'''Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option: 1
Enter contact name: admin
Enter phone number: 3576643
Enter email: admin@gmail.com
Enter address: nanded
Contact 'admin' added successfully!

Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option: 3
Enter name or phone number to search: admin

Found Contact:
Name: admin
Phone: 3576643
Email: admin@gmail.com
Address: nanded'''