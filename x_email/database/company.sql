DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_pk         TEXT,
    user_name       TEXT,
    user_email      TEXT,
    user_password   TEXT,
    user_verified   BOOLEAN,
    user_verification_key       TEXT,
    PRIMARY KEY(user_pk)
) WITHOUT ROWID;


SELECT * FROM users;