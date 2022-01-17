from flask import Flask, render_template, redirect, session
import os
import psycopg2

from controllers.photo_controller import photo_controller
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
from controllers.likes_controller import likes_controller

DB_URL = os.environ.get("DATABASE_URL", "dbname=flask_app")
SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def home():
    return redirect('/signup_login')


app.register_blueprint(photo_controller)
app.register_blueprint(user_controller)
app.register_blueprint(session_controller)
app.register_blueprint(likes_controller)


# @app.route('/like_add')
# # Will add the like to a phot and then redirect back to the same page.
# @app.route('/edit_delete')
# # Take to page where the content can be edited or deleted.
# @app.route('/session/create')
# # from log-in page to create session 'cookie' and then continue onto the main page.
# @app.route('/sessions/destroy')
# # from confirm logout page, destroy the session and end the log in.
# @app.route('/users')
# # take data from sign up page and add to the user TABLE in the DB.
# @app.route('/login')
# # From initail form go to login page
# @app.route('/signup')
# # From the initial form... Go to the sign up page

if __name__ == "__main__":
    app.run(debug=True)
