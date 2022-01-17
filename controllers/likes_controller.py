from flask import Blueprint, request, session, redirect, render_template
from models.likes import insert_likes, delete_like

likes_controller = Blueprint(
    "likes_controller", __name__, template_folder="../templates/pets")


@likes_controller.route('/like', methods=['POST'])
def create():
    user_id = session.get('user_id')
    photo_id = request.form.get('photo_id')

    insert_likes(photo_id, user_id)

    return redirect('/')


@likes_controller.route('/un_like', methods=['POST'])
def destroy():
    user_id = session.get('user_id')
    photo_id = request.form.get('photo_id')
    delete_like(photo_id, user_id)

    return redirect('/')
