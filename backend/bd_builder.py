
'''passwordcheck

-- удаление таблиц если существуют

DROP TABLE IF EXISTS Users, Scenarios, GamesLocations, Enemies;

CREATE TABLE Users(
    user_id INT not NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_nickname text UNIQUE NOT NULL,
    email text UNIQUE NOT NULL,
    upassword VARCHAR(40) NOT NULL,
	CONSTRAINT password_lenght CHECK ( length(upassword) > 8)
);

CREATE TABLE Scenarios(
    Scenarios_id INT not NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description VARCHAR(100) NOT NULL,
    structure jsonb UNIQUE,
    rooms_id VARCHAR(40)
);

CREATE TABLE GamesLocations(
    rooms_id INT not NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description VARCHAR(100) NOT NULL,
    enemies jsonb not NULL
);

CREATE TABLE Enemies(
    enemie_id INT not NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    health INT NOT NULL,
    defence INT NOT NULL,
    damage INT NOT NULL
);

'''