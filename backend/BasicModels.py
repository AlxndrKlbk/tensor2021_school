import psycopg2

class User():

    def __init__(self, fname, lname, ID, city, nick_name, phone_number=None):
        self.__ID = ID
        self.__first_name = fname
        self.__last_name = lname
        self.nickname = nick_name
        self.__city = city
        self.__prone_number = phone_number
        self.__dungeons_ID = None
        self.__games_count = None

    def _get_name(self):
        s = ' '
        return s.join((self.__first_name, self.__last_name))

    def show_person(self):
        print(f'Nickname: {self.nickname}')
        print(f'Name: {self._get_name()}')
        print(f'ID: {self.__ID}')
        print(f'City: {self.__city}')

    def update_user(self):
        pass

    def change_nickname(self):
        pass

    def get_fields(self):
        pass

    def invite_to_lobby(self):
        pass


class GameField():

    def __init__(self):
        self.__name = None
        self.__rooms = None
        self.__players_amount = None
        self.__enemies_list = None
        self.__accessible_for_all = False
        self.__text_nodes = None

    def get_field(self, id):
        pass

    def update_field(self, updates):
        pass


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