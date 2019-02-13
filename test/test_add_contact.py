# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(prefix, maxlen):
    numbers = string.digits
    return prefix + " ".join([random.choice(numbers) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
                    nickname=random_string("nickname", 10), photo=random_string("photo", 20), title=random_string("title", 20), company=random_string("company", 10),
                    address=random_string("address", 20), home=random_string("home", 20), mobile=random_string("mobile", 10), work=random_string("work", 10),
                    fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=" ", bday=("3"), bmonth=("November"), byear=("2019"), aday=("12"), amonth=("December"), ayear=("2019"))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
   # pass
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


