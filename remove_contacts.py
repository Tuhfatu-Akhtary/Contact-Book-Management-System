import save_contacts

def remove_contact(all_contacts):
    name_to_remove = input("Enter the name of the contact you want to remove: ")

    for contact in all_contacts:
        if contact['name'] == name_to_remove:
            all_contacts.remove(contact)
            save_contacts.save_contacts(all_contacts)
            print("Contact removed successfully!")
            return

    print("Contact is not found")
