-- mysql
CREATE TABLE pastes(id INTEGER AUTO_INCREMENT,
    title varchar(80),
    syntax varchar(80),
    name varchar(80),
    email varchar(200) NULL,
    source TEXT,
    html TEXT,
    created datetime,
    lastview datetime,
    ipaddr varchar(20) NULL,
    PRIMARY KEY (id)
);


create table sessions(
session_id CHAR(128) UNIQUE NOT NULL,
atime TIMESTAMP,
data TEXT
);