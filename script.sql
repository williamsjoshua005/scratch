
CREATE TABLE IF NOT EXISTS sc_user (
    id INTEGER NOT NULL,
    name VARCHAR(200) NOT NULL,
    PRIMARY KEY (id)
);


COPY sc_user(id, name)
FROM '/tmp/data.csv'
DELIMITER ','
CSV HEADER;


select current_database();
