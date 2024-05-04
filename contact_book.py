"""A Simple Contact Book."""
import os.path
import csv

from colored import Fore, Back, Style
import emoji


file_name = "contactbook.csv"
choice = ""

print(emoji.emojize(f"{Fore.white}{Back.blue}Welcome To Your Contact Book :waving_hand:{Style.reset}"))

def menu():
    """Main Menu Function."""
    print(emoji.emojize(f"1. {Fore.blue}{Back.green}Add New Contacts{Style.reset} :bust_in_silhouette:"))
    print(emoji.emojize(f"2. {Fore.red}{Back.black}Search Contacts{Style.reset} :magnifying_glass_tilted_left:"))
    print(emoji.emojize(f"3. {Fore.white}{Back.yellow}View Contacts{Style.reset} :eye: :eye:"))
    print(emoji.emojize(f"4. {Fore.red}{Back.blue}Edit Contacts{Style.reset} :books:"))
    print(emoji.emojize(f"5. {Fore.yellow}{Back.green}Delete Contacts{Style.reset} :cross_mark:"))
    print(emoji.emojize(f"6. {Fore.white}{Back.red}Exit{Style.reset} :door:"))

    user_choice = input(emoji.emojize(f"{Fore.green}{Back.blue}Enter Your Selection{Style.reset} :right_arrow: "))
    return user_choice


if not os.path.isfile(file_name):
    print("Creating New File As It Does Not Exist")
    contact_file = open(file_name, "w")
    contact_file.write("")
    contact_file.close()


def add_contact(file_name):
    """Add Contact Function."""
    name = input("Enter The Contact's Name: ")
    phone_number = input(emoji.emojize("Enter The Contact's Phone Number :telephone_receiver: : "))
    email = input("Enter The Contact's Email: ")
    address = input("Enter The Contact's Address: ")
    contact_details = [name, phone_number, email, address]
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(contact_details)
    print(emoji.emojize("Contact Added Successfully. :beaming_face_with_smiling_eyes:"))

def search_contacts(file_path, search_query):
    """Search Contact function."""
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            matches = [row for row in reader if search_query.lower() in [element.lower() for element in row]]
            if matches:
                for index, match in enumerate(matches, start=1):
                    print(f"Match {index}: Name: {match[0]}, Phone Number: {match[1]}, Email: {match[2]}, Address: {match[3]}")
            else: print(emoji.emojize("No Contacts Found Matching Your Search. :frowning_face:"))
    except FileNotFoundError:
        print("No contacts file found. Please add some contacts first.")

def view_contacts(file_path):
    """View Contact Function."""
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, start=1):
                print(f"Contact {index} Name: {row[0]}\t Phone Number: {row[1]}\t Email: {row[2]}\t Address: {row[3]}")
    except FileNotFoundError:
        print(emoji.emojize("No Contacts Found. Add some contacts first. :frowning_face:"))

def delete_contact(file_path):
    """Delete Contact Functiion."""
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            contacts = list(reader)

        if not contacts:
            print(emoji.emojize("No Contacts Available To Delete. :frowning_face:"))
            return
        print("Select A Contact To Delete:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}: Name: {contact[0]}, Phone Number: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")

        contact_index = int(input("Enter The Number Of The Contact To delete: ")) - 1

        if contact_index < 0 or contact_index >= len(contacts):
            print("Invalid Contact Number.")
            return
        del contacts[contact_index]
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print(emoji.emojize("Contact deleted successfully. :thumbs_up:"))
    except FileNotFoundError:
        print("No contacts file found. Please add some contacts first.")
    except ValueError:
        print(emoji.emojize("Invalid Input. Please Enter A Numeric Value. :frowning_face:"))


def edit_contact(file_path):
    """Edit Contact Function."""
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            contacts = list(reader)

        if not contacts:
            print(emoji.emojize("No Contacts Available To Edit. :frowning_face:"))
            return
        print("Select A Contact To Edit:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}: Name: {contact[0]}, Phone Number: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
        contact_index = int(input("Enter The Number Of The Contact To Edit: ")) - 1
        if contact_index < 0 or contact_index >= len(contacts):
            print(emoji.emojize("Invalid Contact Number. :frowning_face:"))
            return
        print("Enter New Details For The Contact. Press ENTER To Skip Editing A Field.")
        name = input(f"Name [{contacts[contact_index][0]}]: ") or contacts[contact_index][0]
        phone_number = input(f"Phone Number [{contacts[contact_index][1]}]: ") or contacts[contact_index][1]
        email = input(f"Email [{contacts[contact_index][2]}]: ") or contacts[contact_index][2]
        address = input(f"Address [{contacts[contact_index][3]}]: ") or contacts[contact_index][3]
        contacts[contact_index] = [name, phone_number, email, address]
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print(emoji.emojize("Contact Updated Successfully. :beaming_face_with_smiling_eyes:"))
    except FileNotFoundError:
        print("No contacts file found. Please add some contacts first.")
    except ValueError:
        print(emoji.emojize("Invalid Input. Please Enter A Numeric Value. :frowning_face:"))
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
        print(emoji.emojize(f"{Fore.white}{Back.blue}Thank You For Using Our Contact Book{Style.reset} :waving_hand:"))
    else:
        print(emoji.emojize("Please Select One Of The Options Below :down_arrow:"))
