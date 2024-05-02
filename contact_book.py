import os.path
import csv




file_name = "contactbook.csv"
choice = ""

print("welcome To Your Contact Book")

def menu():
    print(" 1. Add New Contact \n 2. Search Contacts \n 3. View Contacts \n 4. Edit Contacts \n 5. Delete Contacts \n 6. Exit ")

    user_choice = input("Enter Your Selection ")
    return user_choice


if not os.path.isfile(file_name):
    print("Creating New File As It Does Not Exist")
    contact_file = open(file_name, "w")
    contact_file.write("")
    contact_file.close()


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
    
def search_contacts(file_path, search_query):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            matches = [row for row in reader if search_query.lower() in [element.lower() for element in row]]
            if matches:
                for index, match in enumerate(matches, start=1):
                    print(f"Match {index}: Name: {match[0]}, Phone Number: {match[1]}, Email: {match[2]}, Address: {match[3]}")
            else:print("No contacts found matching your search.")
    except FileNotFoundError:
        print("No contacts file found. Please add some contacts first.")

def view_contacts(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, start=1):
                print(f"Contact {index} Name: {row[0]}\t Phone Number: {row[1]}\t Email: {row[2]}\t Address: {row[3]}")
    except FileNotFoundError:
        print("No Contacts Found. Add some contacts first.")
    
def delete_contact(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            contacts = list(reader)
        
        if not contacts:
            print("No contacts available to delete.")
            return
        print("Select a contact to delete:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}: Name: {contact[0]}, Phone Number: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
        
        contact_index = int(input("Enter the number of the contact to delete: ")) - 1

        if contact_index < 0 or contact_index >= len(contacts):
            print("Invalid contact number.")
            return
        del contacts[contact_index]
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print("Contact deleted successfully.")
    except FileNotFoundError:
        print("No contacts file found. Please add some contacts first.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def edit_contact(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            contacts = list(reader)
        
        if not contacts:
            print("No contacts available to edit.")
            return
        print("Select a contact to edit:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}: Name: {contact[0]}, Phone Number: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
        contact_index = int(input("Enter the number of the contact to edit: ")) - 1
        if contact_index < 0 or contact_index >= len(contacts):
            print("Invalid contact number.")
            return
        print("Enter new details for the contact. Press ENTER to skip editing a field.")
        name = input(f"Name [{contacts[contact_index][0]}]: ") or contacts[contact_index][0]
        phone_number = input(f"Phone Number [{contacts[contact_index][1]}]: ") or contacts[contact_index][1]
        email = input(f"Email [{contacts[contact_index][2]}]: ") or contacts[contact_index][2]
        address = input(f"Address [{contacts[contact_index][3]}]: ") or contacts[contact_index][3]
        contacts[contact_index] = [name, phone_number, email, address]
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print("Contact updated successfully.")
    except FileNotFoundError:
        print("No contacts file found. Please add some contacts first.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


        
        
    



while choice != "6":
    choice = menu()
    
    if (choice == "1"):
        print("If Info N/A, Leave Empty And Press Enter")
        add_contact(file_name)
    elif (choice == "2"):
        search_query = input("Enter Contacts Name: ")
        search_contacts(file_name, search_query) 
        
    elif (choice == "3"):
        view_contacts(file_name)
    elif (choice == "4"):
        edit_contact(file_name)
    elif (choice == "5"):
        delete_contact(file_name)
    elif (choice == "6"):
        print("Thank You For Using Our Contact Book")
    else:
        print("Please Select One Of The Options Below")

