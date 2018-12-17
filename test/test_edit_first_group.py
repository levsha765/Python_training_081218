

from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.test_edit_first_group(Group(name="New_name", header="New_header", footer="New_footer"))
    app.session.logout()
