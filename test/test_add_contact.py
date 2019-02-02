# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Pavel", middlename="Petrovich", lastname="Ivanov", nickname="Petro", photo="C:\\temp\\temp.jpg", title="PP", company="Lenovo", address="Moscow", home ="911", mobile="89020203033", work="02", fax="01", email="petro@gmail.com", email2=" ", email3=" ", homepage=" ", bday="3", bmonth="January", byear="1990", aday="10", amonth="November", ayear="1999")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
