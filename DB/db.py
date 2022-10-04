import logging
from contextlib import contextmanager
from urllib.parse import urlparse
from psycopg2 import pool
from settings.settings import Settings

db_uri = urlparse(Settings.db_uri())
reporting_db_pool = pool.ThreadedConnectionPool(1, 50, user=db_uri.username,
                                             password=db_uri.password,
                                             host=db_uri.hostname,
                                             port=db_uri.port,
                                             database=db_uri.path[1:]
                                             )

class Web_api_db:
    @classmethod
    @contextmanager
    def get_cursor(cls):
        con = reporting_db_pool.getconn()
        try:
            yield con.cursor()
            con.commit()
        finally:
            reporting_db_pool.putconn(con)

    @classmethod
    def update(cls, sql, qryparams):
        with cls.get_cursor() as cursor:
            logging.debug(u'Executing sql: [{0}]'.format(sql.strip()))
            cursor.execute(sql, qryparams)

    @classmethod
    def query(cls, sql, qryparams):
        with cls.get_cursor() as cursor:
            logging.debug(u'Executing sql: [{0}]'.format(sql.strip()))
            cursor.execute(sql, qryparams)
            return cursor.fetchall()

    @classmethod
    def query_single(cls, sql, qryparams):
        with cls.get_cursor() as cursor:
            logging.debug(u'Executing sql: [{0}]'.format(sql.strip()))
            cursor.execute(sql, qryparams)
            return cursor.fetchone()

    @classmethod
    def query_multi_line(cls, sql):
        with cls.get_cursor() as cursor:
            cursor.execute(sql)