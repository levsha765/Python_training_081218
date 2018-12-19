from model.contact import Contact


def test_add_contact(app):
    app.contact.edit_first_contact(Contact(firstname="!4123", middlename="4123", lastname="4123",
                               nickname="4123", company="4123", address="4123",
                               home="4123", mobile="4123", work="4123", fax="4123",
                               email="4123", email2="8123", email3="4123", homepage="4123",
                               bday="27", bmonth="October", byear="1958",
                               aday="30", amonth="June", ayear="1969",
                               address2="4123", phone2="4123", notes="5123"))
