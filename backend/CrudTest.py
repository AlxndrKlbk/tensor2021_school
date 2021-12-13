from objects.MainEntities import Scenario, Enemies, Room, User
from objects.BasicModel import Postgres
import json

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


for i in range(10):
    basic_scenario = {"name": f"scenario{i+1}", "description": "", "structure": "{}", "rooms_id": "1,2,3"}
    basic_scenario = json.dumps(basic_scenario)
    result = postgress.query("INSERT INTO scenarios (description, structure, rooms_id) VALUES (%s,%s,%s) "
                             "ON CONFLICT DO NOTHING RETURNING scenarios_id",
                             (f"text{i}", basic_scenario, "1,2,3"))
    print(result)


for i in range(3):
    basic_room = {"goblin": 2, "ogre": 1, "skeleton": 3}
    basic_room = json.dumps(basic_room)
    result = postgress.query("INSERT INTO gameslocations (description, enemies) VALUES (%s,%s) "
                             "ON CONFLICT DO NOTHING RETURNING rooms_id",
                             ("some amazing description", basic_room))


for name in ['ogre', 'goblin', 'sceleton']:
    result = postgress.query("INSERT INTO enemies (name, health, defence, damage) VALUES (%s,%s,%s,%s) "
                             "ON CONFLICT DO NOTHING RETURNING enemie_id",
                             (name, 5, 2, 2))
