import psycopg2
# connecting to the db .
def get_db_conn():

    conn = psycopg2.connect(
        dbname="bank",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )
    return conn