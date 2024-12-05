def view_contacts(all_contacts):
    if all_contacts!=[]:
        for contact in all_contacts:
            print(f"Name : {contact['name']}")
            print(f"Email : {contact['email']}")
            print(f"Phone Number : {contact['phone_number']}")
            print(f"Address : {contact['address']}")

    else:
        print("No Contact Found")