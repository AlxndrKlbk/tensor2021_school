import aiohttp
from objects.MainEntities import Scenario, Enemies, Room, User
from objects.BasicModel import Postgres
from db_config import config


postgress = Postgres()

postgress.query("INSERT INTO users (user_nickname, email, upassword) VALUES (%s,%s,%s) ON CONFLICT DO NOTHING RETURNING"
                " user_id",
                ('Sanya', 'sanya@mail.ru', 'hardpass1'))

postgress.query("INSERT INTO users (user_nickname, email, upassword) VALUES (%s,%s,%s) ON CONFLICT DO NOTHING RETURNING"
                " user_id",
                ('Boba', 'boba@mail.ru', 'hardpass1'))

user = User("Sanya")

print(user._nickname)
PK = user.find_entity('user_nickname', user._nickname)[0][0]
user._delite_record('user_id', PK)