from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1, 1, database='learning', user='postgres', password='1234', host='localhost' ) 

