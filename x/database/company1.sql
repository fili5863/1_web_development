-- Drop the 'users' table if it exists
DROP TABLE IF EXISTS users;

-- Create the 'users' table
CREATE TABLE users (
    user_pk                 TEXT UNIQUE, -- Primary key for users table
    user_user_name          TEXT UNIQUE, -- Unique username for users
    user_name               TEXT,        -- User's name
    user_email              TEXT UNIQUE, -- Unique email for users
    PRIMARY KEY (user_pk)                -- Primary key constraint
) WITHOUT ROWID;                         -- Without ROWID optimization

-- Insert sample data into the 'users' table
INSERT INTO users VALUES ('1', 'a', 'A', '@a');
INSERT INTO users VALUES ('2', 'b', 'B', '@b');
INSERT INTO users VALUES ('3', 'c', 'B', '@c');

-- Drop the 'pets' table if it exists
DROP TABLE IF EXISTS pets;

-- Create the 'pets' table
CREATE TABLE pets (
    pet_pk                  TEXT UNIQUE, -- Primary key for pets table
    pet_type                TEXT UNIQUE, -- Unique type of pet
    PRIMARY KEY(pet_pk)                   -- Primary key constraint
) WITHOUT ROWID;                         -- Without ROWID optimization

-- Insert sample data into the 'pets' table
INSERT INTO pets VALUES ('1', 'dog');
INSERT INTO pets VALUES ('2', 'cat');

-- Drop the 'users_pets' table if it exists
DROP TABLE IF EXISTS users_pets;

-- Create the 'users_pets' table
CREATE TABLE users_pets (
    user_fk                 TEXT,        -- Foreign key referencing users
    pet_fk                  TEXT,        -- Foreign key referencing pets
    PRIMARY KEY (user_fk, pet_fk)        -- Compound primary key
) WITHOUT ROWID;                         -- Without ROWID optimization

-- Insert sample data into the 'users_pets' table
INSERT INTO users_pets VALUES ('1', '1');
INSERT INTO users_pets VALUES ('1', '2');
INSERT INTO users_pets VALUES ('2', '2');

-- Drop the 'v_users_pets' view if it exists
DROP VIEW IF EXISTS v_users_pets;

-- Create the 'v_users_pets' view
CREATE VIEW v_users_pets AS 
SELECT user_pk, user_name, user_email, pet_type
FROM users
JOIN users_pets ON user_pk = user_fk
JOIN pets ON pet_fk = pet_pk;

-- Select data from the 'v_users_pets' view
SELECT * FROM v_users_pets;




-- SELECT u.user_pk, u.user_name, u.user_email, p.pet_type
-- FROM users u
-- JOIN users_pets up ON u.user_pk = up.user_fk
-- JOIN pets p ON up.pet_fk = p.pet_pk;


-- SELECT user_pk, user_name, user_email, pet_type
-- FROM users
-- JOIN users_pets ON user_pk = user_fk
-- JOIN pets ON pet_fk = pet_pk;

