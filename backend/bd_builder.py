
'''passwordcheck

-- удаление таблиц если существуют

DROP TABLE IF EXISTS Users, Scenarios, GamesLocations, Enemies;

CREATE TABLE Users(
    user_id INT not NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_nickname VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL,
    password VARCHAR(40) NOT NULL (LENGTH > 8)
);

CREATE TABLE Scenarios(
    Scenarios_id INT not NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description VARCHAR(100) NOT NULL,
    structure json UNIQUE,
    rooms_id VARCHAR(40)
);


CREATE TABLE GamesLocations(
    rooms_id INT not NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description VARCHAR(100) NOT NULL,
    enemies json not NULL
);

CREATE TABLE Enemies(
    enemie_id INT not NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    health INT NOT NULL,
    defence INT NOT NULL,
    DAMAGE INT NOT NULL
);

'''