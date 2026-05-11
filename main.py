# Code Your Import statments below to import your Contacts class as well as your search and sorting functions (you will build these yourself!!!!):

# ---------------------------------------- DO NOT MODIFY THE CODE BELOW THIS LINE ! IF YOU MODIFY THE BELOW CODE YOU WILL GET A 0 ! ---------------------------------------- #
# THIS CODE IS NECESSARY TO RUN YOUR FILES! 
#these imports let us create fake data below
#if the import does not work, open your Terminal and type: pip install Faker
from faker import Faker
# random lets the contact_list be extra shuffled so you can do your sorting algorithm
import random
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
