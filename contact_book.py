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
    contact_file.write(" ")
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
    
def view_contacts(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, start=1):
                print(f"Contact {index} Name: {row[0]}\t Phone Number: {row[1]}\t Email: {row[2]}\t Address: {row[3]}")
    except FileNotFoundError:
        print("No Contacts Found. Add some contacts first.")

while choice != "6":
    choice = menu()

    if (choice == "1"):
        print("If Info N/A, Leave Empty")
        add_contact(file_name)
    elif (choice == "2"):
        print("You Have Selected 2")
    elif (choice == "3"):
        view_contacts(file_name)
    elif (choice == "4"):
        print("You Have Selected 4")
    elif (choice == "5"):
        print("You Have Selected 5")
    else:
        print("Please Select One Of The Options Below")
print("Thank You For Using My Contact Book")
