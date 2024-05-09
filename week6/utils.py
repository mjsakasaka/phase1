import mysql.connector

def get_db_data(sql_query: str) -> list:
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    cursor.execute(sql_query)
    data = cursor.fetchall()
    con.close()
    return data

def change_db_data(sql_query: str) -> None:
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    cursor.execute(sql_query)
    con.commit()
    con.close()



