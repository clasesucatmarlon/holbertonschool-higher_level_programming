-- create a new user with full privileges on localhost

-- create: user1
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user1_12345';

-- grant privileges: user1
GRANT ALL ON *.* TO user_0d_1@localhost;
