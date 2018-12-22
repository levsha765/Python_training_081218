

class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.app.open_home_page()
        #self.return_groups_page()


    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)



    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()
        #self.return_groups_page()
        self.app.open_home_page()


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit
        wd.find_element_by_name("update").click()
        #self.return_groups_page()
        self.app.open_home_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[3]/a").click()


    def return_home(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
