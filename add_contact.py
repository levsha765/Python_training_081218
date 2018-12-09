# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
#from contact import Contact

class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        #self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()


    def create_contact(self, wd):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(u"Имя")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(u"Отчество")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(u"Фамилия")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(u"Ник")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(u"Фирма")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(u"Адресс")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("123123")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+79101471414")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("465465")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("456465")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email1@email.ru")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("email1@email.ru")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("email1@email.ru")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("site.ru")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("12")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("March")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[37]").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1955")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("15")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[17]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("March")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[37]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1960")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(u"Адрес2")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(u"Дом")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(u"Описание")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def open_add_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()


    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.create_contact(wd)
        self.Logout(wd)
    

    

    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
