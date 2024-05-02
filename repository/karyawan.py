import psycopg2
import pandas
from config import database as db

def create(request:dict) -> bool:
    affected = False
    sql = f"INSERT INTO karyawan (nama, no_telp) VALUES ('{request['nama']}', '{request['no_telp']}');"
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
    sql = "SELECT * FROM karyawan"
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
def findOne(id:str):
    sql = f"SELECT * FROM karyawan WHERE id = {id}"
    config = db.config()
    try:
        with  psycopg2.connect(**config) as connection:
            with  connection.cursor() as cursor:
                cursor.execute(sql)
                row_karyawan = cursor.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit()
    finally:
        return row_karyawan
def edit(request:dict) -> bool:
    affected = False
    sql = f"UPDATE karyawan SET {request['column']} = '{request['new_value']}'  WHERE id = {request['id']};"
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
    sql = f"DELETE FROM karyawan WHERE id = {id}"
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