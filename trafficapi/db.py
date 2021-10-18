from dataclasses import asdict
from config import MYSQLINFO
import pymysql

from utils import trafficapidata


class SQLConnect:
    def __init__(self) -> None:
        self.tablename = "TrafficStatus_test"
        self._conn = pymysql.connect(**MYSQLINFO)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql: str, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql: str, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def get_exist_UID(self):
        self.execute(f"Select UID from {self.tablename}")
        self.fetchall()

    def update_new_data(self, rawdata: trafficapidata):
        data = asdict(rawdata)
        queryvalue = ",".join([f"`{k}`" for k in data.keys()])
        insertvalue = ",".join([f"`{repr(v)}`" for v in data.values()])
        print(queryvalue)
        print("\n")
        print(insertvalue)
        print(f"INSERT INTO `{self.tablename}` ({queryvalue}) VALUES ({insertvalue})")
        self.execute(
            f"INSERT INTO `{self.tablename}` ({queryvalue}) VALUES ({insertvalue})"
        )
        self.commit()
