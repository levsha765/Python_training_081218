from model.contact import Contact
from random import randrange
import random

def test_edit_first_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    id = random_contact.id
    contact = Contact(firstname="!4123", middlename="4123", lastname="4123",
                               nickname="4123", company="4123", address="4123",
                               home="4123", mobile="4123", work="4123", fax="4123",
                               email="4123", email2="8123", email3="4123", homepage="4123",
                               bday="27", bmonth="October", byear="1958",
                               aday="30", amonth="June", ayear="1969",
                               address2="4123", phone2="4123", notes="5123")
    contact.id = id
    app.contact.edit_contact_by_id(random_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == random_contact.id:
            old_contacts[i] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


# def test_edit_first_contact(app, db, check_ui):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test"))
#     old_contacts = app.contact.get_contact_list()
#     random_contact = randrange(len(old_contacts))
#     contact = Contact(firstname="!4123", middlename="4123", lastname="4123",
#                                nickname="4123", company="4123", address="4123",
#                                home="4123", mobile="4123", work="4123", fax="4123",
#                                email="4123", email2="8123", email3="4123", homepage="4123",
#                                bday="27", bmonth="October", byear="1958",
#                                aday="30", amonth="June", ayear="1969",
#                                address2="4123", phone2="4123", notes="5123")
#     contact.id = old_contacts[random_contact].id
#     app.contact.edit_contact_by_index(random_contact, contact)
#     old_contacts[random_contact] = contact
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


