import psycopg2
from loguru import logger
from loader import postgres_db_user, postgres_db_pass, postgres_db_host, postgres_db_port, postgres_db_name

logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='INFO', rotation='10 MB', compression='zip')


def get_connection():
    conn = psycopg2.connect(
        user=f"{postgres_db_user}",
        password=f"{postgres_db_pass}",
        host=f"{postgres_db_host}",
        port=f"{postgres_db_port}",
        database=f'{postgres_db_name}'
    )
    conn.autocommit = True
    return conn


def connect():
    conn = get_connection()
    cursor = conn.cursor()
    return cursor


def check_database():
    #logger.debug('Check db models')
    cursor = connect()
    try:
        cursor.execute("SELECT tablename FROM pg_catalog.pg_tables;")
        tables = cursor.fetchall()
        res = []

        for table in tables:
            res.append(table[0])

#    if 'table_name' not in res:
        return 'OK'

    except psycopg2.OperationalError as e:
        return f'some operational error: {e}'
