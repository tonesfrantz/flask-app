import psycopg2
from psycopg2.extras import DictCursor


def sql_select(query, param):
