from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="Pavel", middlename="Petrovich", lastname="Ivanov", nickname="Petro",
                                   photo="C:\\temp\\temp.jpg", title="PP", company="Lenovo", address="Moscow",
                                   home="911", mobile="89020203033", work="02", fax="01", email="petro@gmail.com",
                                   email2=" ", email3=" ", homepage=" ", bday="3", bmonth="January", byear="1990",
                                   aday="10", amonth="November", ayear="1999"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
