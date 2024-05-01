
file_name = "contactbook.csv"

def add_contact(file_name):
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contact_details = [name, phone_number, email, address]
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(contact_details)
    print("Contact added successfully.")


def view_contacts(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, start=1):
                print(f"Contact {index}: Name={row[0]}, Phone Number={row[1]}, Email={row[2]}, Address={row[3]}")
    except FileNotFoundError:
        print("No contacts found. Add some contacts first.")


