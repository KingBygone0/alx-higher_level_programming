-- point 1
-- create user with all privileges
CREATE USER IF NOT EXISTS user_0d_1@localhost;
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1_pwd';
