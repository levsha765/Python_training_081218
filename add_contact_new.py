# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture





def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="123", middlename="123", lastname="123",
                                        nickname="123", company="123", address="123",
                                        home="123", mobile="123", work="123", fax="123",
                                        email="123", email2="123", email3="123", homepage="123",
                                        bday="12", bmonth="March", byear="1960",
                                        aday="12", amonth="May", ayear="1961",
                                        address2="123", phone2="123", notes="123"))
    app.Logout()








