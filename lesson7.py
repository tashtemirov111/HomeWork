import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn
def create_table(connection, create_table_sql):
    try:
        cursor = connection = connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


database_nam = 'group_53db'
sql_to_create_emloyees_table = '''
CREATE TABLE employees
'''
my_connection = create_connection(database_nam)
if my_connection is not None:
    print('Connection created successfully')
    # Here will be oprations with
