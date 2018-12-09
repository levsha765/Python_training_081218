# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
import unittest

class AddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_id("LoginForm").submit()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(u"Имя")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(u"Отчество")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(u"Фамилия")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(u"Ник")
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(u"Фирма")
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"Адресс")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("123123")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("+79101471414")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("465465")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("456465")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("email1@email.ru")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("email1@email.ru")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("email1@email.ru")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("site.ru")
        Select(driver.find_element_by_name("bday")).select_by_visible_text("1")
        Select(driver.find_element_by_name("bday")).select_by_visible_text("12")
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("March")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[37]").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1955")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("15")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[17]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("March")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[37]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("1960")
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(u"Адрес2")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(u"Дом")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(u"Описание")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        driver.find_element_by_link_text("Logout").click()
    

    

    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
