from flask import Blueprint, request, session, redirect, render_template
from models.photo import insert_photo, get_all_photos, get_photo, delete_photo, update_photos

photo_controller = Blueprint(
    "photo_controller", __name__, template_folder="../templates/pets")


@photo_controller.route('/home')
@photo_controller.route('/all_pets')
def photos():
    if "user_id" in session and session["user_id"] != None:
        pet_photos = get_all_photos()
        return render_template("pets.html", pet_photos=pet_photos)
    else:
        return redirect('/sigup_login')


# create

# insert

# update

# delete
