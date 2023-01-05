import psycopg2
import sys
import logging
from logging import StreamHandler
from contextlib import closing
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = StreamHandler(stream=sys.stdout)
logger.addHandler(handler)
with closing(psycopg2.connect(            
            user="postgres",
            password="1111",
            host="127.0.0.1",
            port="5432"
            )) as conn:
    with conn.cursor() as cursor:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        insert_query = """ INSERT INTO test (TS, NUMBER)
                        VALUES (generate_series('2022-10-01', '2022-11-01', interval '1 hour'), random()*(1000-0+1)+0)"""
        cursor.execute(insert_query)
        conn.commit()
        print("В таблицу добавлены данные")
        # Вычисляю среднее
        avg_query = '''SELECT TS, avg(NUMBER) as avg_num  FROM test GROUP BY TS ORDER BY TS;'''
        cursor.execute(avg_query)
        msg = cursor.fetchall()
        # Добавляю инфу в логи
        logger.info(msg)