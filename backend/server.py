import aiohttp
from objects.MainEntities import Scenario, Enemies, Room, User
from objects.BasicModel import Postgres
from db_config import config


postgress = Postgres()

postgress.query("INSERT INTO users (user_nickname, email, upassword) VALUES (%s,%s,%s) ON CONFLICT DO NOTHING",
                ('Sanya', 'sanya@mail.ru', 'hardpass1'))

postgress.query("INSERT INTO users (user_nickname, email, upassword) VALUES (%s,%s,%s) ON CONFLICT DO NOTHING",
                ('Boba', 'boba@mail.ru', 'hardpass1'))
