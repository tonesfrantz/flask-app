DROP TABLE users CASCADE;

DROP TABLE photos CASCADE;

DROP TABLE photo_likes CASCADE;

create table users (
    user_id SERIAL NOT null primary key,
    name VARCHAR(100) not null,
    email TEXT not null unique,
    password VARCHAR(255) not null
);

create table photos (
    photo_id SERIAL NOT null primary key,
    user_id INT,
    photo_url TEXT not null,
    caption VARCHAR(255)
);

create table photo_likes (
    photo_id INT,
    user_id INT,
    PRIMARY KEY(photo_id, user_id),
    CONSTRAINT fk_photo FOREIGN KEY(photo_id) REFERENCES photos(photo_id) ON DELETE CASCADE,
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        1,
        'static/images/arlo1.jpeg',
        'arlo1'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        1,
        'static/images/arlo2.jpeg',
        'arlo2'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        2,
        'static/images/arlo3.JPG',
        'arlo3'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        2,
        'static/images/arlo4.jpeg',
        'arlo4'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        3,
        '/static/images/arlo5.JPG',
        'arlo5'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        3,
        '/static/images/arlo6.JPG',
        'arlo6'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        4,
        '/static/images/arlo7.jpeg',
        'arlo7'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        4,
        '/static/images/arlo8.JPG',
        'arlo8'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        5,
        '/static/images/arlo9.JPG',
        'arlo9'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        5,
        '/static/images/arlo10.JPG',
        'arlo10'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        6,
        '/static/images/arlo11.JPG',
        'arlo11'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        6,
        '/static/images/arlo12.jpeg',
        'arlo12'
    );