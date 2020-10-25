import psycopg2
import json

#conn=psycopg2.connect(database='User_game', user='postgres' , password="12345")
conn=psycopg2.connect(host="localhost", database='User_game', user='postgres' , password="12345", port=5432)

cur=conn.cursor()

cur.execute('''

DROP TABLE if exists users CASCADE;
DROP TABLE if exists games;

CREATE TABLE users(
    userId SERIAL NOT NULL PRIMARY KEY UNIQUE,
    name TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
    );

CREATE TABLE games(
    gameId SERIAL NOT NULL PRIMARY KEY UNIQUE,
    userId INTEGER REFERENCES users (userId),
    duration INTEGER,
    difficulty INTEGER,
    size INTEGER,
    completed INTEGER,
    date TEXT
    )
''')


infile= open("sample_data.json")
info= infile.read()
data= json.loads(info)

for key in data:
    cur.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (data[key]['name'], data[key]['email'], data[key]['password']))
    cur.execute('SELECT userId FROM users where email=%s', (data[key]['email'], ))
    current_userid= cur.fetchone()[0]

    cur.execute('INSERT INTO games (userId) VALUES (%s)', (current_userid,))

conn.commit()
cur.close()
conn.close()