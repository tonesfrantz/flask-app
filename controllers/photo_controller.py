from flask import Blueprint, request, session, redirect, render_template
import boto3
import os
from models.photo import insert_photo, get_all_photos, get_photo, delete_photo, update_photos, get_photo_by_type
from werkzeug.utils import secure_filename

ACCESS_KEY_ID = os.environ.get("S3_ACCESS_KEY_ID")
ACCESS_SECRET_KEY = os.environ.get(
    "S3_ACCESS_SECRET_KEY")


BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "pet-peer-photos-local")


s3 = boto3.client('s3',
                  aws_access_key_id=ACCESS_KEY_ID,
                  aws_secret_access_key=ACCESS_SECRET_KEY,
                  )


photo_controller = Blueprint(
    "photo_controller", __name__, template_folder="../templates/pets")

# create


@photo_controller.route('/photo/create')
def create_page():
    return render_template("create.html")


@photo_controller.route('/photo/create/upload', methods=['POST'])
def create_photo_upload():
    user_id = session.get('user_id')
    caption = request.form.get("caption")
    pet_type = request.form.get("pet_type")
    img = request.files['photo']

    if not img:
        return redirect('/photo/create')
    filename = secure_filename(img.filename)
    img.save(filename)
    s3.upload_file(
        Bucket=BUCKET_NAME,
        Filename=filename,
        Key=f'images/{filename}'
    )
    photo_url = f'https://{BUCKET_NAME}.s3.ap-southeast-2.amazonaws.com/images/{filename}'
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


@photo_controller.route('/sort_type', methods=['GET'])
def sort_by_tyoe():
    if "user_id" in session and session["user_id"] != None:
        user_id = session.get("user_id")
        type = request.args.get("type", None)
        if type != None:
            pet_photos = get_photo_by_type(user_id, type)
            return render_template("type.html", pet_photos=pet_photos)
        else:
            return render_template("type.html")
    else:
        return redirect('/signup_login')


@photo_controller.route('/sort_type/post', methods=['POST'])
def display_type():
    pet_type = request.form.get("pet_type")
    return redirect(f'/sort_type?type={pet_type}')
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
    photo = get_photo(photo_id)
    photo_url = photo['photo_url']
    # secure_filename(img.photo_url)
    photo_key = photo_url.replace(
        f'https://{BUCKET_NAME}.s3.ap-southeast-2.amazonaws.com/', "")
    print(photo_url)
    s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=photo_key
    )

    # query to get photo URL... find out current photo URL
    # s3 request to delete file.
    delete_photo(photo_id)
    return redirect('/')
