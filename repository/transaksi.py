import psycopg2
import pandas
from config import database as db

def create(request:dict) -> bool:
    affected = False
    sql = f"INSERT INTO transaksi (tanggal_transaksi, nama_pelanggan, no_telp_pelanggan, id_paket, id_karyawan) VALUES ('{request['tanggal_transaksi']}', '{request['nama_pelanggan']}', '{request['no_telp_pelanggan']}', {request['id_paket']}, {request['id_karyawan']});"
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
    sql = "SELECT * FROM transaksi"
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