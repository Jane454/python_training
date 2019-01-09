from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="changed", header="changed", footer="changed"))
    app.session.logout()
