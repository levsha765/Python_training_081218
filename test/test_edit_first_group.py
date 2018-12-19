

from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Wow1"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="Wow2"))
    app.session.logout()


# def test_modify_group_footer(app):
#     app.session.login(username="admin", password="secret")
#     app.group.test_edit_first_group(Group(footer="New_footer"))
#     app.session.logout()