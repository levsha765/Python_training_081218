

from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Wow1")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    #assert len(old_groups) == len(new_groups)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test1", header="test2"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="Wow2"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


# def test_modify_group_footer(app):
#     app.session.login(username="admin", password="secret")
#     app.group.test_edit_first_group(Group(footer="New_footer"))