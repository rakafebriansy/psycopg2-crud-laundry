import psycopg2
import os
from dotenv import load_dotenv

def createConnection():
    load_dotenv()
    connection = psycopg2.connect(host=os.environ.get('PG_HOST'),
                            port=os.environ.get('PG_PORT'),
                            user=os.environ.get('PG_USER'),
                            password=os.environ.get('PG_PASSWORD'),
                            dbname=os.environ.get('PG_DATABASE'),
                            sslmode='require')
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute('SELECT %s as connected;', ('Connection to postgres successful!',))
    print(cursor.fetchone())

createConnection()