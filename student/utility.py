import pymysql.cursors
from dotenv import dotenv_values

config = dotenv_values(".env")

class DBConnection:
    conn = pymysql.connect(
        host=config.get('HOST'),
        user=config.get('USER'),
        password=config.get('PASSWORD'),
        db=config.get('DATABASE'),
        port=3308,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()