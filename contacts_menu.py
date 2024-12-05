import add_contacts
import view_all_contacts
import remove_contacts
all_contacts=[]

while True:
    print("Welcome to the Contact Management System!")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Remove Contact")
    view_all_contacts.view_contacts(all_contacts)





    option=input("Select option")

    if option == "0":
        print("Thanks for using Contact Management System")
        break

    elif option == "1":
        add_contacts.add_contacts(all_contacts)

    elif option == "2":
        view_all_contacts.view_contacts(all_contacts)

    elif option == "3":
        remove_contacts.remove_contact(all_contacts)

    else:
        print("Choose a valid option")