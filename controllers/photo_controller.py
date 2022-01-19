from flask import Blueprint, request, session, redirect, render_template
from models.photo import insert_photo, get_all_photos, get_photo, delete_photo, update_photos


photo_controller = Blueprint(
    "photo_controller", __name__, template_folder="../templates/pets")

# create


@photo_controller.route('/photo/create')
def create_page():
    return render_template("create.html")


@photo_controller.route('/photo/create/upload', methods=['POST'])
def create_photo_upload():
    user_id = session.get('user_id')
    photo_url = request.form.get("photo_url")
    caption = request.form.get("caption")
    pet_type = request.form.get("pet_type")
    insert_photo(user_id, photo_url, caption, pet_type)
    return redirect('/')

# read


@photo_controller.route('/home')
@photo_controller.route('/all_pets')
def photos():
    if "user_id" in session and session["user_id"] != None:
        user_id = session.get("user_id")
        pet_photos = get_all_photos(user_id)
        return render_template("pets.html", pet_photos=pet_photos)
    else:
        return redirect('/signup_login')


@photo_controller.route('/enlarge/<photo_id>')
def enlarge(photo_id):
    pet = get_photo(photo_id)
    return render_template('enlarge.html', pet=pet)


@photo_controller.route('/sort_type', methods=['GET', 'POST'])
def sort_by_tyoe():
    if "user_id" in session and session["user_id"] != None:
        user_id = session.get("user_id")
        pet_type = request.form.get("pet_type")
        if pet_type == None:
            return render_template("type.html")
        elif pet_type != None:
            pet_photos = get_all_photos(user_id)
            return render_template("type.html", pet_photos=pet_photos, pet_type=pet_type)
    else:
        return redirect('/signup_login')

# edit


@photo_controller.route('/edit_delete', methods=['POST'])
def edit():
    photo_id = request.form.get("photo_id")
    pet = get_photo(photo_id)
    return render_template("edit_delete.html", pet=pet)


# update
@photo_controller.route('/photo/<photo_id>', methods=['POST'])
def update(photo_id):
    photo_url = request.form.get("photo_url")
    caption = request.form.get("caption")
    pet_type = request.form.get("pet_type")
    update_photos(photo_id, photo_url, caption, pet_type)
    return redirect('/')


# delete
@photo_controller.route('/photo/<photo_id>/delete', methods=['POST'])
def delete(photo_id):
    delete_photo(photo_id)
    return redirect('/')
