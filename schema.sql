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
    caption VARCHAR(255),
    pet_type TEXT
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
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo1.jpeg',
        'arlo1',
        'dog'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        1,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo2.jpeg',
        'arlo2',
        'dog'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        2,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo3.JPG',
        'arlo3',
        'dog'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        2,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo4.jpeg',
        'arlo4',
        'cat'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        3,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo5.JPG',
        'arlo5',
        'fish'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        3,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo6.JPG',
        'arlo6',
        'other'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        4,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo7.jpeg',
        'arlo7',
        'horse'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        4,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo8.JPG',
        'arlo8',
        'horse'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        5,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo9.JPG',
        'arlo9',
        'fish'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        5,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo10.JPG',
        'arlo10',
        'dog'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        6,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo11.JPG',
        'arlo11',
        'dog'
    );

INSERT INTO
    photos (user_id, photo_url, caption, pet_type)
VALUES
    (
        6,
        'https://pet-peer-photos.s3.ap-southeast-2.amazonaws.com/images/arlo12.jpeg',
        'Big Stick... I love a big stick!',
        'dog'
    );