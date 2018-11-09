"""The database configuration file."""
url = ""


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(url)
    return con


def create_table():
    """Method to create table."""
    con = connection(url)
    curr = con.cursor()

    queries = tables()
    for t in queries:
        curr.execute(t)
    con.commit()


def destroy_table():
    """Method to destroy tables."""
    pass
