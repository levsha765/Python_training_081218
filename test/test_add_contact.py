# -*- coding: utf-8 -*-


from model.contact import Contact



def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#, ids=["firstname","lastname"]

    # contact = Contact(firstname="123", middlename="123", lastname="123",
    #                            nickname="123", company="123", address="123",
    #                            home="123", mobile="123", work="123", fax="123",
    #                            email="123", email2="123", email3="123", homepage="123",
    #                            bday="12", bmonth="March", byear="1960",
    #                            aday="12", amonth="May", ayear="1961",
    #                            address2="123", phone2="123", notes="123")





