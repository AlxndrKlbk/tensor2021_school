from backend.objects.BasicModel import Postgres
import json


class User(Postgres):
    _TABLE = "Users"
    _FIELDS_MAPPING = {}

    def __init__(self, nick_name):
        self._nickname = nick_name
        self._dungeons_ID = None

    def show_person(self):
        print(f'Nickname: {self._nickname}')

    def update_user(self):
        pass

    def change_nickname(self, new_nickname):

        self._nickname = new_nickname
        pass

    def get_fields(self):
        pass

    def invite_to_lobby(self):
        pass


class Scenario(Postgres):
    _TABLE = "Scenarios"
    _FIELDS_MAPPING = {}

    def __init__(self):
        self._name = None
        self._rooms = None
        self._players_amount = None
        self._enemies_list = None
        self._accessible_for_all = False
        self._text_nodes = None
        self.__description = None
        self._active_user = None

    def __hash__(self):
        return hash((self._name, self._active_user))

    @classmethod
    async def get_scenario_list(self):
        sql_sentence = f"SELECT * from {self._TABLE} LIMIT 20"
        return self.query(sql_sentence)

    @classmethod
    async def _create_record(self):
        values_from_mapping = []
        keys_from_mapping = ""
        for key, val in self._FIELDS_MAPPING.items():
            keys_from_mapping += str(key) + ','
            if key == 'structure':
                values_from_mapping.append(json.dumps(val))
            else:
                values_from_mapping.append(val)

        values = '%s,'*len(self._FIELDS_MAPPING.keys())
        sql_sentence = f"INSERT INTO {self._TABLE} ({keys_from_mapping[0:-1]}) " \
                       f"VALUES({values[0:-1]}) RETURNING rooms_id"

        result = self.query(sql_sentence, values_from_mapping)
        return result[0][0]


class Room(Postgres):
    _TABLE = "GamesLocations"
    _FIELDS_MAPPING = {}

    def __init__(self):
        self._description = None
        self._enemies = None
        self._special_requirements = None


    #это костыль
    @classmethod
    async def _create_record(self):
        values_from_mapping = []
        keys_from_mapping = ""
        for key, val in self._FIELDS_MAPPING.items():
            keys_from_mapping += str(key) + ','
            if key == 'enemies':
                values_from_mapping.append(json.dumps(val))
            else:
                values_from_mapping.append(val)

        values = '%s,'*len(self._FIELDS_MAPPING.keys())
        sql_sentence = f"INSERT INTO {self._TABLE} ({keys_from_mapping[0:-1]}) " \
                       f"VALUES({values[0:-1]}) RETURNING rooms_id"

        result = self.query(sql_sentence, values_from_mapping)
        return result[0][0]


class Enemies(Postgres):
    _TABLE = "Enemies"
    _FIELDS_MAPPING = {}

    def __init__(self):
        self._name = None
        # self._defence = None
        # self._damage = None
        # self._health = None
        # self.__skills = None
        self._active_properties = {'hp': None, 'defence': None, 'damage': None,'skills' : None}

    @classmethod
    def __get_enemie_json(self, db_id):
        """
        this function take json representation of enemie from db

        :param db_id:
        :return:
        """
        return None

    def __getattr__(self, attr_name):
        if attr_name in self.active_properties:
            return self._dict[attr_name]
        return super().__getattribute__(attr_name)

    def __set_effects(self, effects):
        for effect in effects.items():
            self._active_properties += effects[effect]
