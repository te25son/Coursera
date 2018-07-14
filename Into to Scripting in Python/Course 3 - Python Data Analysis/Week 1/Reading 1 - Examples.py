"""
Course 3
Week 1 - Reading 1 - Examples
"""


def space():
    print('')


contact_list = {
    'John Doe': '1-101-233-4567',
    'Abe Froman': '1-800-728-7243',
    'Betty Bean Ross': '1-888-123-4567'
}

print(
    """
    \rLOOKUP A KEY
    \r------------
    """
)


def lookup(contacts, name):
    """
    Lookup name in contacts and return the phone number
    or a message if name not in contacts.
    """
    if name in contacts:
        return contacts[name]
    else:
        return "Name Not In Contacts"


print(lookup(contact_list, "Abe Froman"))
print(lookup(contact_list, "Jose Virano"))

space()

# we can make this function even simpler using the GET function


def lookup2(contacts, name):
    """
    Lookup name in contacts and return the phone number
    or a message if name not in contacts.
    """
    return contacts.get(name, "Name Not In Contacts")


print(lookup2(contact_list, 'John Doe'))
print(lookup2(contact_list, 'Henry John Frankfurt'))

space()

print(
    """
    \rITERATE OVER DICTIONARY
    \r-----------------------
    """
)

# we can iterate over a dictionary directly


def print_contacts(contacts):
    """
    Prints the keys of a given contact list
    """
    for name in contacts:
        print(name)


print_contacts(contact_list)

space()


def print_contact_list(contacts):
    """
    prints the keys and values of a given contact list
    """
    for name in contacts:
        print(name, ':', contacts[name])


print_contact_list(contact_list)

space()

print(
    """
    \rORDER DICTIONARIES
    \r------------------
    """
)


def ordered_contacts(contacts):
    """
    Print the keys and values of a given contact list
    in alphabetical order.
    """
    keys = contacts.keys()  # assigns a list of the keys in a dictionary to variable keys
    names = sorted(keys)
    for name in names:
        print(name, ':', contacts[name])


ordered_contacts(contact_list)

space()

print(
    """
    \rUPDATE A DICTIONARY
    \r-------------------
    """
)


def add_contact(contacts, name, number):
    """
    Adds a contact to an existing contact list
    """
    if name in contacts:
        print("Contact Already Exists")
    else:
        contacts[name] = number


add_contact(contact_list, 'Abe Froman', '1-800-728-7243')
add_contact(contact_list, 'Suzy Onli', '1-777-321-7654')
ordered_contacts(contact_list)

space()


def update_contact(contacts, name, newnumber):
    """
    Updates an existing contacts number in given contact list
    """
    if name in contacts:
        contacts[name] = newnumber
    else:
        print('%s does not exist in contact list' % name)


update_contact(contact_list, 'Suzy Onli', '1-899-154-6433')
update_contact(contact_list, 'Henry Ford', '1-800-NEW-CARS')
ordered_contacts(contact_list)

# OR, if we wanted to add a contact that's not that or update an existing,
# we could do this...


def add_update_contact(contacts, name, number):
    """
    Updates an existing contact and adds a new contact if contact doesn't
    already exist
    """
    contacts[name] = number
