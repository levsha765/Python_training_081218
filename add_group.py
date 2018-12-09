# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class AddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()


    def create_group(self, wd, name, header, footer):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill form group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # submit group creation
        wd.find_element_by_name("submit").click()


    def return_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_xpath("//html").click()


    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd,  username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, name="zaq1", header="xsw2", footer="cde3")
        self.return_groups_page(wd)
        self.Logout(wd)


    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, name="", header="", footer="")
        self.return_groups_page(wd)
        self.Logout(wd)
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()