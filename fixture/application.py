from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:


    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)



    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    # def login(self, username, password):
    #     wd = self.wd
    #     self.open_home_page()
    #     wd.find_element_by_name("user").click()
    #     wd.find_element_by_name("user").clear()
    #     wd.find_element_by_name("user").send_keys(username)
    #     wd.find_element_by_name("pass").clear()
    #     wd.find_element_by_name("pass").send_keys(password)
    #     wd.find_element_by_id("LoginForm").submit()


    # def open_groups_page(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("groups").click()

    # def open_add_contact_page(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("add new").click()


    # def create_group(self, group):
    #     wd = self.wd
    #     self.open_groups_page()
    #     # init group creation
    #     wd.find_element_by_name("new").click()
    #     # fill form group
    #     wd.find_element_by_name("group_name").click()
    #     wd.find_element_by_name("group_name").clear()
    #     wd.find_element_by_name("group_name").send_keys(group.name)
    #     wd.find_element_by_name("group_header").click()
    #     wd.find_element_by_name("group_header").clear()
    #     wd.find_element_by_name("group_header").send_keys(group.header)
    #     wd.find_element_by_name("group_footer").click()
    #     wd.find_element_by_name("group_footer").clear()
    #     wd.find_element_by_name("group_footer").send_keys(group.footer)
    #     # submit group creation
    #     wd.find_element_by_name("submit").click()
    #     self.return_groups_page()

    # def create_contact(self, contact):
    #     wd = self.wd
    #     self.open_add_contact_page()
    #     # init contect creation
    #     wd.find_element_by_name("firstname").click()
    #     # fill form contact
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys(contact.firstname)
    #     wd.find_element_by_name("middlename").clear()
    #     wd.find_element_by_name("middlename").send_keys(contact.middlename)
    #     wd.find_element_by_name("lastname").clear()
    #     wd.find_element_by_name("lastname").send_keys(contact.lastname)
    #     wd.find_element_by_name("nickname").clear()
    #     wd.find_element_by_name("nickname").send_keys(contact.nickname)
    #     wd.find_element_by_name("company").click()
    #     wd.find_element_by_name("company").clear()
    #     wd.find_element_by_name("company").send_keys(contact.company)
    #     wd.find_element_by_name("address").click()
    #     wd.find_element_by_name("address").clear()
    #     wd.find_element_by_name("address").send_keys(contact.address)
    #     wd.find_element_by_name("home").clear()
    #     wd.find_element_by_name("home").send_keys(contact.home)
    #     wd.find_element_by_name("mobile").clear()
    #     wd.find_element_by_name("mobile").send_keys(contact.mobile)
    #     wd.find_element_by_name("work").clear()
    #     wd.find_element_by_name("work").send_keys(contact.work)
    #     wd.find_element_by_name("fax").clear()
    #     wd.find_element_by_name("fax").send_keys(contact.fax)
    #     wd.find_element_by_name("email").clear()
    #     wd.find_element_by_name("email").send_keys(contact.email)
    #     wd.find_element_by_name("email2").clear()
    #     wd.find_element_by_name("email2").send_keys(contact.email2)
    #     wd.find_element_by_name("email3").clear()
    #     wd.find_element_by_name("email3").send_keys(contact.email3)
    #     wd.find_element_by_name("homepage").clear()
    #     wd.find_element_by_name("homepage").send_keys(contact.homepage)
    #     Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
    #     Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
    #     wd.find_element_by_name("bmonth").click()
    #     Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
    #     wd.find_element_by_xpath(
    #         "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[37]").click()
    #     wd.find_element_by_name("byear").clear()
    #     wd.find_element_by_name("byear").send_keys(contact.byear)
    #     wd.find_element_by_name("aday").click()
    #     Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
    #     wd.find_element_by_xpath(
    #         "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[17]").click()
    #     wd.find_element_by_name("amonth").click()
    #     Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
    #     wd.find_element_by_xpath(
    #         "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[37]").click()
    #     wd.find_element_by_name("ayear").click()
    #     wd.find_element_by_name("ayear").clear()
    #     wd.find_element_by_name("ayear").send_keys(contact.ayear)
    #     wd.find_element_by_name("address2").click()
    #     wd.find_element_by_name("address2").clear()
    #     wd.find_element_by_name("address2").send_keys(contact.address2)
    #     wd.find_element_by_name("phone2").clear()
    #     wd.find_element_by_name("phone2").send_keys(contact.phone2)
    #     wd.find_element_by_name("notes").clear()
    #     wd.find_element_by_name("notes").send_keys(contact.notes)
    #     wd.find_element_by_xpath(
    #         "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
    #     self.return_home()


    # def return_groups_page(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("groups").click()
    #     wd.find_element_by_xpath("//html").click()

    # def return_home(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("home").click()
    #     wd.find_element_by_xpath("//html").click()


    # def Logout(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()