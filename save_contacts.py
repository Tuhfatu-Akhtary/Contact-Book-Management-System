def save_contacts(all_contacts):
    with open("contacts.csv","w") as fp:
        for contact in all_contacts:
            line=f"{contact['name']},{contact['email']},{contact['phone_number']},{contact['address']}"
            fp.write(line)