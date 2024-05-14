import mysql.connector

def get_db_data(sql_query: str, params = None) -> list:
    if params is None:
        params = ()
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    cursor.execute(sql_query, params=params)
    data = cursor.fetchall()
    con.close()
    return data

def change_db_data(sql_query: str, params = None) -> None:
    if params is None:
        params = ()
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    cursor.execute(sql_query, params=params)
    con.commit()
    con.close()

username = "test"
data = get_db_data("SELECT id, name, username FROM member WHERE username = %s", (username, ))
print(data)
print(data == [])