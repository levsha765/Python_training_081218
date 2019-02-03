from model.group import Group
from random import randrange
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = Group(name="Wow1")
    random_group = random.choice(old_groups)
    id = random_group.id
    group.id = id
    #group.id = old_groups[index].id
    app.group.modify_group_by_id(random_group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == random_group.id:
            old_groups[i] = group
    #old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_modify_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="Wow1")
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     #assert len(old_groups) == len(new_groups)
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



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
