# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="group1", header="group1", footer="group1"))
    new_groups = app.group.get_group_list()
   # убеждаемся что длина нового списка больше на одну запись, True
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    # убеждаемся что длина нового списка больше на одну запись, True
    assert len(old_groups) + 1 == len(new_groups)
