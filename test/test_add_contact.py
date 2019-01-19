# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
import random
import string
import re
from random import  randint

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_day():
    day = list(range(1,32))
    return str(random.choice(day))

def random_month():
    month = ["January", "February","March","April","May","June","July","August","September","October","November",
             "December"]
    return random.choice(month)

def random_year():
    year = list(range(1,2020))
    return str(random.choice(year))


testdata = [Contact(firstname="", middlename="", lastname="",
                               nickname="", company="", address="",
                               home="", mobile="", work="", fax="",
                               email="", email2="", email3="", homepage="",
                               #bday="", bmonth="", byear="",
                               #aday="", amonth="", ayear="",
                               address2="", phone2="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 15), nickname=random_string("nickname", 10),
            company=random_string("company", 10), address=random_string("address", 10),
            home=random_string("home", 10), mobile=random_string("mobile", 10),
            work=random_string("work", 10), fax=random_string("fax", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10),
            homepage=random_string("homepage", 10), bday=random_day(), bmonth=random_month(),
            byear=random_year(), aday=random_day(), amonth=random_month(), ayear=random_year(),
            address2=random_string("address2", 10), phone2=random_string("phone2", 10), notes=random_string("notes", 10)
            )
    for i in range(5)
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(firstname="123", middlename="123", lastname="123",
    #                            nickname="123", company="123", address="123",
    #                            home="123", mobile="123", work="123", fax="123",
    #                            email="123", email2="123", email3="123", homepage="123",
    #                            bday="12", bmonth="March", byear="1960",
    #                            aday="12", amonth="May", ayear="1961",
    #                            address2="123", phone2="123", notes="123")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#, ids=["firstname","lastname"]





