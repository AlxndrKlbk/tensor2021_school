DROP TABLE IF EXISTS Users, Scenarios, GamesLocations, Enemies;

CREATE TABLE Users(
    user_id SERIAL PRIMARY KEY,
    user_nickname VARCHAR(40) UNIQUE NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL,
    upassword VARCHAR(40) NOT NULL,
	CONSTRAINT password_lenght CHECK ( length(upassword) > 8)
);

CREATE TABLE Scenarios(
    Scenarios_id SERIAL PRIMARY KEY,
    description VARCHAR(100) NOT NULL,
    structure jsonb,
    rooms_id VARCHAR(40)
);

CREATE TABLE GamesLocations(
    rooms_id SERIAL PRIMARY KEY,
    name VARCHAR(20) not NULL,
    description VARCHAR(100) NOT NULL,
    enemies jsonb not NULL
);

CREATE TABLE Enemies(
    enemie_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    health INT NOT NULL,
    defence INT NOT NULL,
    damage INT NOT NULL
);