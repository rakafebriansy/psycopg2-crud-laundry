import psycopg2
from config import database as db

def create(request:dict):
    affected = False
    sql = f"INSERT INTO paket (jenis, harga) VALUES ('{request['jenis']}', {request['harga']});"
    print(sql)
    config = db.config()

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                affected = cursor.rowcount
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        input()
    finally:
        print(affected)
        return affected

    