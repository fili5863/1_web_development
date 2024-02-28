
DROP TABLE IF EXISTS bands;
CREATE TABLE bands(
    band_pk           TEXT,
    band_name         TEXT,
    PRIMARY KEY(band_pk)
)WITHOUT ROWID;

CREATE INDEX index_band_name ON bands(band_name);

INSERT INTO bands VALUES ("1", "Led Zeppelin");
INSERT INTO bands VALUES ("2", "The Clash");
INSERT INTO bands VALUES ("3", "Black Sabbath");

SELECT * FROM bands ORDER BY band_pk ASC;

-- ############################################### LABELS

DROP TABLE IF EXISTS labels;

CREATE TABLE labels(
    label_pk            TEXT,
    label_name          TEXT,
    PRIMARY KEY(label_pk)
) WITHOUT ROWID;

INSERT INTO labels VALUES("1", "Atlantic Records");
INSERT INTO labels VALUES("2", "Epic Records");
INSERT INTO labels VALUES("3", "Vertigo Records");

SELECT * FROM labels ORDER BY label_pk ASC;

-- ############################################### BANDS ACTIVE

DROP TABLE IF EXISTS bands_active;

CREATE TABLE bands_active(
    band_active_fk             TEXT,
    band_active_status         BOOLEAN,
    FOREIGN KEY (band_active_fk) REFERENCES bands(band_pk),
    PRIMARY KEY(band_active_fk)
)WITHOUT ROWID;

INSERT INTO bands_active VALUES ("1", FALSE);
INSERT INTO bands_active VALUES ("2", FALSE);
INSERT INTO bands_active VALUES ("3", TRUE);

SELECT * FROM bands_active ORDER BY band_active_fk ASC;



-- ############################################### ALBUMS

DROP TABLE IF EXISTS albums;

CREATE TABLE albums(
    album_pk            TEXT,
    album_band_fk     TEXT,
    album_title         TEXT,
    album_year          INTEGER,
    album_label_fk      TEXT,
    FOREIGN KEY (album_label_fk) REFERENCES labels(label_pk),
    FOREIGN KEY (album_band_fk)  REFERENCES bands(band_pk),
    PRIMARY  KEY (album_pk, album_band_fk, album_label_fk)

) WITHOUT ROWID;

INSERT INTO albums VALUES("1", "1", "Led Zeppelin II", 1969,"1");
INSERT INTO albums VALUES("2", "1", "Houses of the Holy", 1973,"1");
INSERT INTO albums VALUES("3", "2", "Combat Rock", 1982,"2");
INSERT INTO albums VALUES("4", "3", "Paranoid", 1970,"3");
INSERT INTO albums VALUES("5", "3", "Master of Reality", 1971,"3");

CREATE INDEX index_album_title ON albums(album_title);

-- ############################################### BANDMEMBERS

DROP TABLE IF EXISTS members;

CREATE TABLE members(
    member_pk                  TEXT,
    member_band_fk             TEXT,
    member_name                TEXT,
    member_last_name           TEXT,
    PRIMARY KEY(member_pk),
    FOREIGN KEY(member_band_fk) REFERENCES bands(band_pk)
) WITHOUT ROWID;

INSERT INTO members VALUES("1","1", "Jimmy", "Page");
INSERT INTO members VALUES("2","1", "Robert", "Plant");
INSERT INTO members VALUES("3","1", "Jon", "Bonham");
INSERT INTO members VALUES("4","1", "John", "Paul Jones");
INSERT INTO members VALUES("5","2","Joe", "Strummer");

SELECT * FROM members ORDER BY member_pk ASC;


-- ############################################### INSTRUMENTS

DROP TABLE IF EXISTS instruments;

CREATE TABLE instruments(
    instrument_pk       TEXT,
    instrument_name     TEXT,
    
    PRIMARY KEY(instrument_pk)
) WITHOUT ROWID;

INSERT INTO instruments VALUES ("1", "Vocals");
INSERT INTO instruments VALUES ("2", "Guitar");
INSERT INTO instruments VALUES ("3", "Bass");
INSERT INTO instruments VALUES ("4", "Drums");
INSERT INTO instruments VALUES ("5", "Keys");

SELECT * FROM instruments;

-- ############################################### MEMBER INSTRUMENTS

DROP TABLE IF EXISTS member_instruments;

CREATE TABLE member_instruments(
    member_fk       TEXT,
    instrument_fk   TEXT,
    FOREIGN KEY(member_fk) REFERENCES member(member_pk),
    FOREIGN KEY(instrument_fk) REFERENCES instruments(instrument_pk),
    PRIMARY KEY(member_fk, instrument_fk)

) WITHOUT ROWID;

INSERT INTO member_instruments VALUES ("1","2");
INSERT INTO member_instruments VALUES ("2","1");
INSERT INTO member_instruments VALUES ("3","4");
INSERT INTO member_instruments VALUES ("4","3");
INSERT INTO member_instruments VALUES ("5","1");



-- ###############################################
--##### Making a view table to connect the band with albums and label 
DROP VIEW IF EXISTS v_band_album; 


CREATE VIEW v_band_album AS  
SELECT band_pk ,band_name, album_title, label_name, band_active_status
FROM bands 
JOIN albums ON band_pk = album_band_fk 
JOIN labels ON  album_label_fk=label_pk
JOIN bands_active ON band_pk = band_active_fk; 
SELECT * FROM v_band_album;

-- ###############################################

DROP VIEW IF EXISTS v_band_members;

CREATE VIEW v_band_members AS 
SELECT band_name, member_name, member_last_name, instrument_name
FROM bands
JOIN members ON band_pk = member_band_fk
JOIN member_instruments ON member_pk = member_instruments.member_fk
JOIN instruments ON instrument_pk = member_instruments.instrument_fk;

SELECT * FROM v_band_members;

