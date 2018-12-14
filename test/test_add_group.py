# -*- coding: utf-8 -*-


from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="zaq1", header="xsw2", footer="cde3"))
    app.session.Logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.Logout()

