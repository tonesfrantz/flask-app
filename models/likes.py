import database

# CRUD


def insert_likes(user_id, photo_id):
    database.sql_write("INSERT into photo_likes (user_id, photo_id) VALUES (%s, %s);", [
                       user_id, photo_id])
