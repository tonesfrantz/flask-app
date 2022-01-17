from flask import Blueprint, session, request, redirect, render_template
from models.user import delete_user, get_all_users, get_user_by_email, get_user_by_id, update_user, insert_user

user_controller = Blueprint(
    "user_controller", __name__, template_folder="../templates/users")


@user_controller.route("/signup", methods=['POST'])
def signup():
    error = request.args.get("error", None)
    return render_template("signup.html", error=error)


@user_controller.route("/users", methods=['POST'])
def create_user():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    password2 = request.form.get("password2")
    if password != password2:
        return redirect("/signup?error=Invalid+password+confirmation")
    user = insert_user(name, email, password)
    session['user_id'] = user['user_id']
    session['user_name'] = user['name']
    return redirect("/all_pets")

    # INSERT INTO users(columns, ...) VALUES( % s,) RETURNING *


@user_controller.route("/user_list")
def user_list():
    users = get_all_users()
    return render_template("user_list.html", users=users)


@user_controller.route("/user/<id>/edit", methods=["POST"])
def user_edit(id):
    user = get_user_by_id(id)
    return render_template("user_edit.html", user=user)


@user_controller.route("/user/<id>/delete", methods=["POST"])
def delete(id):
    delete_user(id)
    return redirect("/user_list")
