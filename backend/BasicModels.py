import psycopg2


class User:

    def __init__(self, fname, lname, ID, city, nick_name, phone_number=None):
        self._ID = ID
        self._first_name = fname
        self._last_name = lname
        self._nickname = nick_name
        self._city = city
        self._prone_number = phone_number
        self._dungeons_ID = None
        self._games_count = None

    def _get_name(self):
        s = ' '
        return s.join((self._first_name, self._last_name))

    def show_person(self):
        print(f'Nickname: {self._nickname}')
        print(f'Name: {self._get_name()}')
        print(f'ID: {self._ID}')
        print(f'City: {self._city}')

    def update_user(self):
        pass

    def change_nickname(self):
        pass

    def get_fields(self):
        pass

    def invite_to_lobby(self):
        pass


class Scenario:

    def __init__(self):
        self._name = None
        self._rooms = None
        self._players_amount = None
        self._enemies_list = None
        self._accessible_for_all = False
        self._text_nodes = None
        self._active_user = None

    def __hash__(self):
        return hash((self._name, self._active_user))

    @classmethod
    def get_scenario_json(self, db_id):
        """
        This function take json representation of scenario from db

        :param db_id: scenraio id in db
        :return: json representation of object
        """
        return None

    @classmethod
    def update_scenatio(self, updates):
        """
        This function set users setting for his active scenario

        :param updates: json with users settings
        :return: Nothing
        """
        pass


class Room:

    def __init__(self):
        self._description = None
        self._enemies = None
        self._special_requirements = None

    def __fit_setting(self, config):
        pass


class Enemies:

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

class DataBase():

    def __init__(self, config):
        self.connection = None
        self.connection = psycopg2.connect(**config)

    def query(self, sql, args):
        cursor = self.connection.cursor()
        cursor.execute(sql, args)
        return cursor

    def insert(self, sql, args):
        cursor = self.query(sql, args)
        id = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return id

    def insertmany(self, sql, args):
        cursor = self.connection.cursor()
        cursor.executemany(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount

    def update(self, sql, args):
        cursor = self.query(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount

    def fetch(self, sql, args):
        rows = []
        cursor = self.query(sql, args)
        if cursor.with_rows:
            rows = cursor.fetchall()
        cursor.close()
        return rows

    def fetchone(self, sql, args):
        row = None
        cursor = self.query(sql, args)
        if cursor.with_rows:
            row = cursor.fetchone()
        cursor.close()
        return row

    def __del__(self):
        if self.connection != None:
            self.connection.close()