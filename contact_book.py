contacts = []
def display_menu():
    print("Contact book Menu")
    print("1.Add a contact")
    print("2.Search for a contact")
    print("3.Update a contact")
    print("4.delete the contact")
    print("5.display the contact")
    print("6.Exit")
def add_contact():
    name =input("Enter the name of contact: ")
    email = input("Enter the email: ")
    phone = input("Enter the phone number: ")
    contact = {"Name": name, "Email": email,"Phone": phone}
    contacts.append(contact)
    print("Contact added successfully")
def search_contact():
    search_term =input("Enter the name or email of the contact to search: ")
    found_contacts=[]
    for contact in contacts:
        if search_term.lower() in contact["Name"].lower() or search_term.lower() in contact["email"].lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Matching contacts found:")
        for contact in found_contacts:
            print("Name:",contact["Name"])
            print("Email:",contact["email"])
            print("Phone:",contact["Phone"])
            print("-------------------")
    else:
        print("No matching contacts are found")
def update_contact():
    name=input("Enter the name of the contact to update:")
    found_contact = None
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            found_contact=contact
            break
    if found_contact:
        print("Contact Found.Enter the new details:")
        found_contact["Name"] = input("Enter the new name")
        found_contact["email"] = input("Enter the new email")
        found_contact["Phone"] = input("Enter the new phone")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")
def delete_contact():
    name=input("Enter the name of the contact to delete")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contacts are successfully deleted")
            break
    else:
        print("Contact not found")
def display_all_contacts():
    if contacts:
        print("All Contacts:")
        for contact in contacts:
            print("Name:",contact["Name"])
            print("Email:",contact["email"])
            print("Phone:",contact["Phone"])
            print("-------------------")
    else:
        print("No contacts found")
while True:
    display_menu()
    choice=int(input("Enter your choice(1-6): "))


    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        print("Exiting the program....")
        break
    else:
        print("Invalid choice.Please enter a valid option (1-6).")