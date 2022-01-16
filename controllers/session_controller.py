from flask import Blueprint, session, request, redirect, render_template
import bcrypt
from models.user import delete_user, get_user_by_email, insert_user, get_user_by_id, get_all_users, update_user


session_controller = Blueprint(
    "session_controller", __name__, template_folder="../templates/session")


@session_controller.route("/login", methods=['POST'])
def loginpage():
    error = request.args.get("error", None)
    return render_template("login.html", error=error)


@session_controller.route("/session/create", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = get_user_by_email(email)
    password_valid = user and bcrypt.checkpw(
        password.encode(), user["password"].encode())

    if password_valid:
        session["user_id"] = user["user_id"]
        session["user_name"] = user["name"]
        return redirect('/home')
    else:
        return redirect("/login?error=Incorrect+username+or+password")


@session_controller.route('/signup_login')
def signup_login_page():
    if "user_id" in session and session["user_id"] != None:
        return redirect("/all_pets")
    else:
        return render_template('signup_login.html')


@session_controller.route("/logout")
def inital_logout():
    return render_template("logout.html")


@session_controller.route("/sessions/destroy", methods=["POST"])
def logout():
    session["user_id"] = None
    return redirect("/signup_login")
