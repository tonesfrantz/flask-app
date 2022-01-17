from flask import Blueprint, request, session, redirect, render_template
from models.likes import get_all_likes
from models.photo import insert_photo, get_all_photos, get_photo, delete_photo, update_photos


photo_controller = Blueprint(
    "photo_controller", __name__, template_folder="../templates/pets")


@photo_controller.route('/home')
@photo_controller.route('/all_pets')
def photos():
    if "user_id" in session and session["user_id"] != None:
        user_id = session.get("user_id")
        pet_photos = get_all_photos(user_id)
        return render_template("pets.html", pet_photos=pet_photos)
    else:
        return redirect('/signup_login')


@photo_controller.route('/edit_delete', methods=['POST'])
def edit():
    photo_id = request.form.get("photo_id")
    pet = get_photo(photo_id)
    return render_template("edit_delete.html", pet=pet)
# create

# insert

# update


@photo_controller.route('/photo/<photo_id>', methods=['POST'])
def update(photo_id):
    photo_url = request.form.get("photo_url")
    caption = request.form.get("caption")
    update_photos(photo_id, photo_url, caption)
    return redirect('/')


# delete
