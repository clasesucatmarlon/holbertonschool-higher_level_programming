-- create a new database and a user

-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user: user2
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY "user_0d_2_pwd";

-- give the user access
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
