import psycopg2
from backend.db_config import config


class Postgres:
    _DATABASE = config
    _TABLE = None
    _FIELDS_MAPPING = None

    @classmethod
    def _connect(cls):
        return psycopg2.connect(**cls._DATABASE)

    @classmethod
    def query(cls, sql, *args):
        connection = cls._connect()
        cursor = connection.cursor()
        cursor.execute(sql, *args)
        connection.commit()
        cursor.close()
        return cursor

    @classmethod
    def _create_record(self, pk):
        values_from_mapping = " "
        for keys, val in self.__dict__.items():
            if keys in self._FIELDS_MAPPING.keys():
                values_from_mapping += str(val) + ","
        sql_sentence = f"INSERT INTO {self._TABLE}  VALUES ({values_from_mapping[0:-1]});"
        print(sql_sentence)
        self.query(sql_sentence, values_from_mapping)

    @classmethod
    def _update_record(self, pk, data):
        "data - словарь, в котором содержится имя столбца и значение, которое в него надо вписать"
        table_name = self._TABLE
        for key, val in data.items():
            sql_sentence = f"UPDATE {table_name} SET {key} = {val} where id = {pk}  "
            self.query(sql_sentence, val)

    @classmethod
    def _read_record(self, pk):
        table_name = self._TABLE
        sql_sentence = f"SELECT * from {table_name} where id = {pk}"
        print(self.query(sql_sentence, None))

    @classmethod
    def _delite_record(self, pk):
        table_name = self._TABLE
        sql_sentence = f"DELETE from {table_name} where id = {pk}"
        self.query(sql_sentence, None)

    @classmethod
    def _get_by_pk(cls, pk):
        conn = cls._connect()
        cur = conn.cursor()

        cur.execute(
            """
                SELECT * 
                FROM :table
                WHERE id = :pk
            """,
            {'table': cls._TABLE, 'pk': pk}
        )
        result = {}
        record = cur.fetchone()
        for idx, col in enumerate(cur.description):
            result[col] = record[idx]
        conn.close()
        return result


if __name__ == '__main__':

    database = Postgres()
    print("database connected successfully")

