from model.contact import Contact
from random import randrange

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="!4123", middlename="4123", lastname="4123",
                               nickname="4123", company="4123", address="4123",
                               home="4123", mobile="4123", work="4123", fax="4123",
                               email="4123", email2="8123", email3="4123", homepage="4123",
                               bday="27", bmonth="October", byear="1958",
                               aday="30", amonth="June", ayear="1969",
                               address2="4123", phone2="4123", notes="5123")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

