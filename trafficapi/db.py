from sqlalchemy import create_engine, types
from sqlalchemy.engine.base import Connection
from config import MYSQLINFO
    engine = create_engine(
        f'mysql+pymysql://{MYSQLINFO["user"]}:{MYSQLINFO["password"]}@{MYSQLINFO["host"]}/{MYSQLINFO["db"]}'
    )
    con: Connection