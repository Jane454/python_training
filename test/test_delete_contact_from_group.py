from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_delete_contact_from_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New_group1", header="header1", footer="footer1"))

    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(firstname="New_Created", middlename="Petrovich", lastname="Ivanov", nickname="Petro", photo="C:\\temp\\temp.jpg",
                                    title="PP", company="Lenovo", address="Moscow", home ="911", mobile="89020203033", work="02", fax="01",
                                    email="petro@gmail.com", email2=" ", email3=" ", homepage=" ", bday="3", bmonth="January", byear="1990", aday="10",
                                    amonth="November", ayear="1999")))

    all_groups = db.get_group_list()
    all_contacts = db.get_contact_list()

    contact = random.choice(all_contacts)

    for item in range(len(all_groups)):
        if contact in list(db.get_contacts_in_group(all_groups[item])):
            app.contact.delete_contact_from_group(all_groups[item].id, contact)

    new_contacts = db.get_contact_list()
#    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)