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
    CONSTRAINT fk_photo FOREIGN KEY(photo_id) REFERENCES photos(photo_id),
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

INSERT INTO
    users (name, email, password)
VALUES
    ('user1', 'user1', 'user1');

INSERT INTO
    users (name, email, password)
VALUES
    ('user2', 'user2', 'user2');

INSERT INTO
    users (name, email, password)
VALUES
    ('user3', 'user3', 'user3');

INSERT INTO
    users (name, email, password)
VALUES
    ('user4', 'user4', 'user4');

INSERT INTO
    users (name, email, password)
VALUES
    ('user5', 'user5', 'user5');

INSERT INTO
    users (name, email, password)
VALUES
    ('user6', 'user6', 'user6');

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        1,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo1.jpeg',
        'arlo1'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        1,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo2.jpeg',
        'arlo2'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        2,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo3.JPG',
        'arlo3'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        2,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo4.jpeg',
        'arlo4'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        3,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo5.JPG',
        'arlo5'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        3,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo6.JPG',
        'arlo6'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        4,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo7.jpeg',
        'arlo7'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        4,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo8.JPG',
        'arlo8'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        5,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo9.JPG',
        'arlo9'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        5,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo10.JPG',
        'arlo10'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        6,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo11.JPG',
        'arlo11'
    );

INSERT INTO
    photos (user_id, photo_url, caption)
VALUES
    (
        6,
        '/Users/anthonyfrantz/sei/project2/flask-app/testing photos/arlo12.jpeg',
        'arlo12'
    );