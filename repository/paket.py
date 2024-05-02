import psycopg2
import pandas
from config import database as db

def create(request:dict) -> bool:
    affected = False
    sql = f"INSERT INTO paket (jenis, harga) VALUES ('{request['jenis']}', {request['harga']});"
    print(sql)
    config = db.config()

    try:
        with  psycopg2.connect(**config) as connection:
            with  connection.cursor() as cursor:
                cursor.execute(sql)
                affected = cursor.rowcount
                connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit()
    finally:
        return affected
def findAll() -> pandas.DataFrame:
    sql = "SELECT * FROM paket"
    config = db.config()
    try:
        with  psycopg2.connect(**config) as connection:
            with  connection.cursor() as cursor:
                cursor.execute(sql)
                rows_paket = cursor.fetchall()
                column_names = []
                for column_name in cursor.description:
                    column_names.append(column_name[0])
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit()
    finally:
        df_paket = pandas.DataFrame(rows_paket, columns=column_names, index=[i+1 for i in range(len(rows_paket))])
        return df_paket
def edit(column:str,new_value:str,id:str) -> bool:
    affected = False
    new_value = f"\'{new_value}\'" if column == "jenis" else new_value
    sql = f"UPDATE paket SET {column} = {new_value}  WHERE id = {id};"
    config = db.config()
    try:
        with  psycopg2.connect(**config) as connection:
            with  connection.cursor() as cursor:
                cursor.execute(sql)
                affected = cursor.rowcount
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit()
    finally:
        return affected
def delete(id:str) -> bool:
    sql = f"DELETE FROM paket WHERE id = {id}"
    config = db.config()
    try:
        with  psycopg2.connect(**config) as connection:
            with  connection.cursor() as cursor:
                cursor.execute(sql)
                affected = cursor.rowcount
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit()
    finally:
        return affected