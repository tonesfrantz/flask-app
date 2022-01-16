import database

# All Database functionality relating to pets.

# CRUD
# --Create
# --Read
# --Update
# --Delete


# INSERT

def insert_photo(user_id, photo_url, caption):
    database.sql_write("INSERT INTO photos (user_id, photo_url, caption VALUES(%s, %s, %s);", [
                       user_id, photo_url, caption])

# READ


def get_photo(photo_id):
    results = database.sql_select(
        "SELECT * FROM photos WHERE photo_id = %s;", [photo_id])
    result = results[0]
    return result

# READ_ALL


def get_all_photos():
    results = database.sql_select("SELECT * FROM photos;", [])
    return results

# UPDATE


def update_photos(user_id, photo_url, caption):
    database.sql_write("UPDATE photos SET user_id = %s, photo_url= %s, caption = %s;" [
                       user_id, photo_url, caption])

# DELETE


def delete_photo(photo_id):
    database.sql_write("DELETE FROM photos WHERE photo_id = %s;", [photo_id])
