contacts={}
def add_contact():
    name=input("Enter name:")
    phone=input("Enter phone number:")
    contacts[name]=phone
    print("Contact added!\n")
def view_contacts():
    if not contacts:
        print("no contacts saved.\n")
    else:
        print("\ncontact List:")
        for name,phone in contacts.items():
            print(f"{name}:{phone}")
        print()
def search_contacts():
    name=input("Enter name to search:")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}\n")
    else:
        print("contact not found.\n")
def delete_contact():
    name=input("Enter name to delete:")
    if name in contacts:
        del contacts[name]
        print("contact deleted.\n")
    else:
        print("contact not found.\n")
def menu():
    while True:
        print("=== Contact book ===")
        print("1.Add contact")
        print("2.view contact")
        print("3.search contact")
        print("4.delete contact")
        print("5.exit")

        choice=input("choose an option(1-5):")
        if choice =='1':
            add_contact()
        elif choice =='2':
            view_contacts()
        elif choice =='3':
            search_contacts()
        elif choice =='4':
            delete_contact()
        elif choice =='5':
            print("goodbye!")
        else:
            print("invalid option. try again.\n")
menu()           
