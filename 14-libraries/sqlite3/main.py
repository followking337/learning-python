import sqlite3
from sqlite3 import Error


def open_connection():
    try:
        connection = sqlite3.connect('database.db')  # establish connection
        cursor = connection.cursor()                 # create query
        print('connected successfully...\n')
        return connection, cursor
    except sqlite3.Error:
        print('an error has occurred')


def close_connection(connection):
    try:
        connection.commit()  # update connection
        connection.close()   # closure of the connection
    except:
        print('an error has occurred at connection closing')
    else:
        print('\nconnection closed successfully...')


# getters
def consult_all(cursor):
    sql = 'SELECT * FROM usuario'
    cursor.execute(sql)       # execute SQL sentence
    data = cursor.fetchall()  # store registers from SQL sentence in variable
    return data


def consult_id(cursor, id):
    sql = 'SELECT * FROM usuario WHERE id=?'
    cursor.execute(sql, (id,))
    data = cursor.fetchall()
    return data


# setters
def insert(cursor, data):
    sql = 'INSERT INTO usuario (nombre, apellido) VALUES (?, ?)'
    cursor.execute(sql, data)


def insert_various(cursor, data):
    sql = 'INSERT INTO usuario (nombre, apellido) VALUES (?, ?)'
    cursor.executemany(sql, data)


def update(cursor, id, name, surname):
    sql = 'UPDATE usuario SET nombre=?, apellido=? WHERE id=?'
    cursor.execute(sql, (name, surname, id))


# deleter
def delete(cursor, id):
    sql = 'DELETE FROM usuario WHERE id=?'
    cursor.execute(sql, (id,))


# TESTS:
connection, cursor = open_connection()

# sql = '''CREATE TABLE IF NOT EXISTS usuario(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nombre TEXT NOT NULL,
#     apellido TEXT NOT NULL
#     )'''
# cursor.execute(sql)

# sql = 'DROP TABLE accountant'
# cursor.execute(sql)

# data = ('Miriam', 'Fernandez')
# insert(cursor, data)

# data = [('Pablo', 'España'), ('Jaime', 'Perez'), ('Kiko', 'Rivera')]
# insert_various(cursor, data)

data = consult_all(cursor)
# print(data, type(data), len(data))
for register in data:
    print(register[1], register[2])

# data = consult_id(cursor, 8)
# print(data, type(data), len(data))
# if len(data) > 0:
#     print(data[0][1], data[0][2])
# else:
#     print('ID not exist')

# update(cursor, 13, 'Kiko', 'Rivera')

# delete(cursor, 20)

close_connection(connection)
