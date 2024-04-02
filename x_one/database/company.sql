PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS users;

CREATE TABLE roles(
    role_pk                 TEXT,
    role_name               TEXT,
    PRIMARY KEY(role_pk)
) WITHOUT ROWID;

INSERT INTO roles(role_pk, role_name) VALUES('1', 'admin');

SELECT * FROM roles;

DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_pk                 TEXT,
    user_name               TEXT,
    user_email              TEXT UNIQUE,
    user_password           TEXT,
    user_role_fk               TEXT, 
    PRIMARY KEY(user_pk)
    FOREIGN KEY(user_role_fk) REFERENCES roles(role_pk)
) WITHOUT ROWID;

INSERT INTO users(user_pk, user_name, user_email, user_password, user_role_fk) VALUES('1', 'Admin Jensen', 'admin@user.com', 'adminPassword', '1');


SELECT * FROM users;
