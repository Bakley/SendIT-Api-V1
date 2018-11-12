"""The database configuration file."""
import os
import psycopg2

url = "dbname = 'parcel' user = 'postgres' host ='localhost' port ='5432' password='mypassword'"


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    """Require a url."""
    con = connection(url)
    return con


def create_table():
    """Method to create table."""
    conn = connection(url)
    curr = conn.cursor()
    queries = tables(query1, query2)

    for t in queries:
        curr.execute(t)
    conn.commit()


def tables(self):
    """Creating the schema."""
    query1 = """
    CREATE TABLE IF NOT EXISTS users(
        userid serial PRIMARY KEY,
        email varchar NOT NULL,
        password varchar NOT NULL,
        role varchar NOT NULL,

    )
    """
    query2 = """
    CREATE TABLE IF NOT EXISTS orders(
        orderid serial PRIMARY KEY,
        parcel varchar(50) NOT NULL,
        weight integer(10) NOT NULL,
        price integer(10) NOT NULL,
        destination varchar(25) NOT NULL,
    )"""


def destroy_table():
    """Method to destroy tables."""
    conn = connection(url)
    curr = conn.cursor()
    orders = 'DROP TABLE IF EXISTS orders CASCADE'
    users = 'DROP TABLE IF EXISTS users CASCADE'

    queries = [orders, users]
    for t in queries:
        curr.execute(t)
    conn.commit()
