import aiohttp
from objects.MainEntities import Scenario, Enemies, Room, User
from objects.BasicModel import Postgres
from db_config import config


postgress = Postgres()

postgress.query(f"INSERT INTO users VALUES ('user_nickname', 'email', 'upassword')",
                ('Sanya', 'sanya@mail.ru', 'hardpass'))

