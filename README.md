# Pet - Peer

sei-anz-seifxr06 - Project 2 - [Live Version](https://powerful-everglades-60027.herokuapp.com)

# Design Brief

A website that offers users the ability to log-in, share and like photos of pets. Photos are rated by popularity and comments can be edited by users of their own photos.

# How to Use

Sign-up on the login page. Navigate the site and upload images. Enjoy the Pet joy. (like your favourite)

# Tech_used:

-   HTML
-   CSS
-   Python
-   Heroku
-   SQL Database
-   S3 Storgage Service.

# Planning:

-   See planing folder:
    <img src = "./pet_peer/planning/Pet_Peer_Planning.png" width = "250">
    <img src = "./pet_peer/planning/Pet_Peer_planning2.png" width = "250" >
    planning_diagrams-Page-1.jpg
    planning_diagrams-Page-2.jpg

-   Order of execution:

1. Create DB's from a setup.sql file.
2. INSERT test DATA into both tables. (decided on 3 tables in the end)
3. Create base.html file
4. Make database controller.
5. create controllers for both users and photo data bases.

-   Create S3 account and make INSERT_URL command send to Database.

6. Log in verification.

# Database Table SETUP.SQL (for development and testing)

-   see 'schema.sql' -
-   possible insert code below for planning... refer later
    <!-- INSERT INTO photo_likes (user_id, photo_id) VALUES (1, 1); -->
    <!-- DELETE FROM photo_likes WHERE user_id = 1 AND photo_id = 1; -->

# Challenges:

-   Setting up Amazon S3 to link with the App.
-   CSS
-   Picture size was not reliable as they were not cropped before uploading, this causes size issues.
-   Making the app more interesing and creative was challenging.

# flask-app

<!-- Heroku -->

https://powerful-everglades-60027.herokuapp.com

<!-- Heroku App Link -->

https://powerful-everglades-60027.herokuapp.com/signup_login

<!-- Github -->

https://github.com/tonesfrantz/pet_peer.git
