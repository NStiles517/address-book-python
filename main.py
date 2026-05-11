# Code Your Import statments below to import your Contacts class as well as your search and sorting functions (you will build these yourself!!!!):

# ---------------------------------------- DO NOT MODIFY THE CODE BELOW THIS LINE ! IF YOU MODIFY THE BELOW CODE YOU WILL GET A 0 ! ---------------------------------------- #
# THIS CODE IS NECESSARY TO RUN YOUR FILES! 
#these imports let us create fake data below
#if the import does not work, open your Terminal and type: pip install Faker
from algorithms import binary_search, quick_sort
from faker import Faker
# random lets the contact_list be extra shuffled so you can do your sorting algorithm
import random

from phone_information import Contact
#fake lets us create fake data
fake = Faker()

# Creates 11 instances of the Contact class (WHICH YOU MUST BUILD -- SEE PHONE_INFORMATION.PY), 10 of which use entirely random fake data
# NOTE: all of these calls (fake.first_name(), etc) return a string 
person1 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person2 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person3 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person4 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person5 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person6 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person7 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person8 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person9 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person10 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person11 = Contact("Stephen", "Colbert", fake.phone_number())

# THIS IS THE CONTACT LIST YOU WILL BE USING BELOW to SEARCH THROUGH
contact_list = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10, person11]
# THE LIST HAS BEEN SHUFFLED. THIS WILL BE RANDOM EVERY TIME. YOU HAVE NO IDEA WHERE ANY CONTACT IS!
random.shuffle(contact_list)
# ---------------------------------------- DO NOT MODIFY THE CODE ABOVE THIS LINE ! IF YOU MODIFY THE ABOVE CODE YOU WILL GET A 0 ! ---------------------------------------- #

# Code the remainder of your program below. See assignment for requirements.
while user_input != 4:
  print("Press 1 to show all contacts list, Press 2 to add a contact, Press 3 to search for a specific contact, Press 4 to QUIT")
  user_input = input("enter your choice here: ")
  if user_input == "1":
    quick_sort(contact_list)
    for contact in contact_list:
      print(contact.first_name, contact.last_name, contact.phone_number)
  elif user_input == "2":
    if len(contact_list) >= 20:
      print("Sorry, you cannot add more than 20 contacts.")
    else:
      first_name = input("Enter the first name of the contact: ")
      last_name = input("Enter the last name of the contact: ")
      phone_number = input("Enter the phone number of the contact: ")
      new_contact = Contact(first_name, last_name, phone_number)
      contact_list.append(new_contact)
      quick_sort(contact_list)
      print("Contact added successfully.")

  elif user_input == "3":
    print("Please enter the first name and last name of the contact you want to search for.")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    target_contact = Contact(first_name, last_name, "")
    index = binary_search(contact_list, 0, len(contact_list) - 1, target_contact)
    if index != -1:
        print(target_contact.first_name + " " + target_contact.last_name + "'s phone number is:", contact_list[index].phone_number)
    else:
        print("That contact was not found in the contact list.")
  
  elif user_input == "4":
    print("Goodbye!")  
else:
   print("invalid input, please try again")
