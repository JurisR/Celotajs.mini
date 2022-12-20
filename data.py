import psycopg2
import os

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")

dsn = "host={} dbname={} user={} password={}".format(DB_HOST, DB_NAME, DB_NAME,
                                                     DB_PASSWORD)


#table setup
def create_table1():
  conn = psycopg2.connect(dsn)
  c = conn.cursor()
  c.execute("""CREATE TABLE lietotaji
                (user_id serial PRIMARY KEY, username varchar(10) UNIQUE NOT NULL, vards varchar(8) NOT NULL, uzvards varchar(8) NOT NULL);"""
            )
  conn.commit()
  conn.close()
  return "Table 1 ok"


def create_table2():
  conn = psycopg2.connect(dsn)
  c = conn.cursor()
  c.execute("""CREATE TABLE zinojumi
                (user_id serial PRIMARY KEY,username VARCHAR(10), zinojums TEXT);"""
            )
  conn.commit()
  conn.close()
  return "Table 2 ok"


def del_table(zinojumi):
  conn = psycopg2.connect(dsn)
  c = conn.cursor()
  c.execute("""DROP TABLE zinojumi""")
  conn.commit()
  conn.close()
  return "Table gone"

##Adds user profile to database
def add_user(username, vards, uzvards):
  conn = psycopg2.connect(dsn)
  c = conn.cursor()
  c.execute(
    """INSERT INTO lietotaji(username ,vards ,uzvards)   	                        
    VALUES('{}','{}','{}');""".format(username, vards, uzvards))
  c.close()
  conn.commit()
  conn.close()
  return "User added"

#Adds message entry to database
def add_entry(user_id, zinojums):
  conn = psycopg2.connect(dsn)
  c = conn.cursor()
  c.execute(
    """INSERT INTO zinojumi(user_id,zinojums)VALUES('{}','{}');""".format(user_id, zinojums))
  c.close()
  conn.commit()
  conn.close()
  return "Entry ok"

#Calls Database to recieve user_id and username
def get_user_and_id():
  conn = psycopg2.connect(dsn)
  c = conn.cursor()
  c.execute(""" SELECT user_id, username FROM lietotaji  """)
  atbilde = c.fetchall()
  c.close()
  conn.commit()
  conn.close()
  return atbilde

def getName_and_id():
  conn = psycopg2.connect(dsn)
  c = conn.cursor()
  c.execute("""
SELECT
    vards,
    uzvards,
    zinojums
FROM
    lietotaji
JOIN zinojumi
    ON lietotaji.user_id = zinojumi.user_id;""")
  saraksts = c.fetchall()
  c.close()
  conn.commit()
  conn.close()
  return saraksts