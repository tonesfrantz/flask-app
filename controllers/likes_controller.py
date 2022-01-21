from flask import Blueprint, request, session, redirect, render_template
from models.likes import insert_likes, delete_like
from models.photo import get_all_Desc_most_popular

likes_controller = Blueprint(
    "likes_controller", __name__, template_folder="../templates/pets")

# create


@likes_controller.route('/like', methods=['POST'])
def create():
    user_id = session.get('user_id')
    photo_id = request.form.get('photo_id')
    redirect_path = request.form.get('redirect_path', "/")
    insert_likes(photo_id, user_id)

    return redirect(redirect_path)

# delete


@likes_controller.route('/un_like', methods=['POST'])
def destroy():
    user_id = session.get('user_id')
    photo_id = request.form.get('photo_id')
    redirect_path = request.form.get('redirect_path', "/")
    delete_like(photo_id, user_id)

    return redirect(redirect_path)

# read-most popular


@likes_controller.route('/most_popular')
def photos():
    user_id = session.get("user_id")
    pet_photos = get_all_Desc_most_popular(user_id)
    return render_template("most_popular.html", pet_photos=pet_photos)
