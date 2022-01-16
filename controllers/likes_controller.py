from flask import Blueprint, request, session, redirect, render_template
from models.likes import insert_likes

likes_controller = Blueprint(
    "likes_controller", __name__, template_folder="../templates/pets")


@likes_controller.route('/like', methods=['POST'])
def create():
    user_id = request.get('pet['user_id']')
    photo_id =
