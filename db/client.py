import psycopg2
from src import posgresql_config
from loguru import logger

logger.add(f'src/log/{__name__}.log', format='{time} {level} {message}', level='INFO', rotation='10 MB', compression='zip')


def get_connection():
    database = posgresql_config.db_name
    conn = psycopg2.connect(
        user=f"{posgresql_config.db_user}",
        password=f"{posgresql_config.db_password}",
        host=f"{posgresql_config.db_host}",
        port=f"{posgresql_config.db_port}",
        database=f'{database}'
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
