import database

# CRUD


def insert_likes(photo_id, user_id):
    database.sql_write("INSERT into photo_likes (photo_id, user_id) VALUES (%s, %s);", [
                       photo_id, user_id])


def get_all_likes(photo_id):
    results = database.sql_select(
        "SELECT * FROM photo_likes", [photo_id])
    return results
