-- RESETTER
DROP TABLE IF EXISTS counter;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS phones;



PRAGMA foreign_keys = ON;


DROP TABLE IF EXISTS counter;
CREATE TABLE counter(
    total_users      INTEGER
);

INSERT INTO counter VALUES(0);

SELECT * FROM counter;



DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_pk                 TEXT,
    user_name               TEXT,
    user_updated_at         TEXT,
    user_deleted_at         TEXT,
    user_email              TEXT UNIQUE,
    user_password           TEXT,
    PRIMARY KEY(user_pk)
) WITHOUT ROWID;

-- IF YOU WANT TO SEARCH IN YOUR DB, YOU HAVE TO INDEX

CREATE INDEX idx_username ON users(user_name);


-- CREATE TRIGGER THAT COUNTS THE TOTAL USERS EVERY TIME A NEW IS INSERTED
CREATE TRIGGER IF NOT EXISTS trigger_update_total_users
AFTER INSERT ON users
BEGIN
    UPDATE counter SET total_users = total_users + 1;
END;

-- TRIGGER FOR UPDATED AT ON CHANGE
CREATE TRIGGER IF NOT EXISTS trigger_update_user
AFTER UPDATE ON users
BEGIN
    UPDATE users 
    SET user_updated_at = "Wed 14 Feb 2024" WHERE user_pk=NEW.user_pk;
END;

/* CREATE TRIGGER IF NOT EXISTS trigger_delete_user AFTER UPDATE ON users
BEGIN
    UPDATE users
    SET user_deleted_at = "Wed 14 Feb 2024 NOW" WHERE user_pk=NEW.user_pk;
END; */


-- SEED
INSERT INTO users VALUES("1", "Juan", "0", "0", "one@one.com", "password");
INSERT INTO users VALUES("2", "Two", "0", "0", "two@two.com", "password");
INSERT INTO users VALUES("3", "Three", "0", "0", "three@three.com", "password");
INSERT INTO users VALUES("4", "Four", "0", "0", "four@four.com", "password");

UPDATE users SET user_name = "Samuel" WHERE user_pk = "1";
UPDATE users SET user_deleted_at = CURRENT_TIMESTAMP WHERE user_pk = "1";

SELECT * FROM users;


DROP TABLE IF EXISTS phones;

CREATE TABLE phones(
    phone_user_fk       TEXT,
    phone               TEXT,
    PRIMARY KEY(phone_user_fk, phone), 
    -- FOREIGN KEY(phone_user_fk) REFERENCES users(user_pk) ON DELETE CASCADE
    FOREIGN KEY(phone_user_fk) REFERENCES users(user_pk) ON DELETE RESTRICT
) WITHOUT ROWID;

-- SEED
INSERT INTO phones VALUES("1", "111");
INSERT INTO phones VALUES("1", "112");
INSERT INTO phones VALUES("3", "333");

SELECT * FROM phones;




PRAGMA foreign_keys = ON;
DELETE FROM users WHERE user_pk = "1";
DELETE FROM phones WHERE phone_user_fk = "1";

SELECT * FROM phones;

DELETE FROM users WHERE user_pk = "1";






DROP TABLE IF EXISTS items;

CREATE TABLE items(
    item_id         TEXT,
    item_title      TEXT,
    item_price      NUMERIC,
    PRIMARY KEY(item_id)
) WITHOUT ROWID;


INSERT INTO items VALUES ("1", "One", 10.10);
INSERT INTO items VALUES ("2", "Two", 10.10);
INSERT INTO items VALUES ("3", "Three", 10.10);

SELECT * FROM items;


