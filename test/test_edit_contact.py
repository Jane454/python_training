# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Pavel", middlename="Petrovich", lastname="Ivanov", nickname="Petro",
                                   photo="C:\\temp\\temp.jpg", title="PP", company="Lenovo", address="Moscow",
                                   home="911", mobile="89020203033", work="02", fax="01", email="petro@gmail.com",
                                   email2=" ", email3=" ", homepage=" ", bday="3", bmonth="January", byear="1990",
                                   aday="10", amonth="November", ayear="1999"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.edit_first_contact(Contact(firstname="Roman", middlename="Dmitrich", lastname="Sidorov", nickname="Petro", photo="C:\\temp\\temp.jpg", title="PP", company="Lenovo", address="Moscow", home ="911", mobile="89020203033", work="02", fax="01", email="petro@gmail.com", email2=" ", email3=" ", homepage=" ", bday="3", bmonth="January", byear="1990", aday="10", amonth="November", ayear="1999"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)