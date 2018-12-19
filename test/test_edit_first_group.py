

from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="Wow1"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="Wow2"))


# def test_modify_group_footer(app):
#     app.session.login(username="admin", password="secret")
#     app.group.test_edit_first_group(Group(footer="New_footer"))
