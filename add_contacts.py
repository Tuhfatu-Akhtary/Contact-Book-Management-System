import save_contacts

def add_contacts(all_contacts):
    name=input("Enter Contact Name: ")
    email=input("Enter Contact Email: ")
    phone_number=input("Enter Contact Phone Number: ")
    address=input("Enter Contact Address: ")

    for contact in all_contacts:
        if contact["phone_number"] == phone_number:
            print("Error: This phone number is already associated with another contact.")
            return all_contacts


    contact={
        "name" : name,
        "email" : email,
        "phone_number" : phone_number,
        "address": address,

    }

    all_contacts.append(contact)
    save_contacts.save_contacts(all_contacts)
    print("Contact Added Successfully")

    return all_contacts