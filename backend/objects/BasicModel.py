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
        try:
            result = cursor.fetchall()
        except psycopg2.ProgrammingError:
            result = None

        connection.commit()
        cursor.close()
        return result

    @classmethod
    async def _create_record(self):
        values_from_mapping = ""
        keys_from_mapping = ""
        for keys, val in self._FIELDS_MAPPING.items():
            keys_from_mapping += str(keys) + ','
            values_from_mapping += str(val) + ','
        values_from_mapping = values_from_mapping[0:-1]
        values_from_mapping = tuple(map(lambda x: int(x) if x.isdigit() else x, values_from_mapping.split(sep=',')))
        values = '%s,'*len(self._FIELDS_MAPPING.keys())

        sql_sentence = f"INSERT INTO {self._TABLE} ({keys_from_mapping[0:-1]}) " \
                       f"VALUES({values[0:-1]}) RETURNING enemie_id"

        result = self.query(sql_sentence, values_from_mapping)
        return result[0][0]

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
    def _delite_record(self,col_name ,pk):
        table_name = self._TABLE
        sql_sentence = f"DELETE from {table_name} WHERE {col_name} = '{pk}'"
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

    @classmethod
    async def find_entity(self, column_name, val):
        table_name = self._TABLE
        sql_sentence = f"SELECT * from {table_name} WHERE {column_name} = '{val}'"
        return self.query(sql_sentence, None)

if __name__ == '__main__':

    database = Postgres()
    print("database connected successfully")

