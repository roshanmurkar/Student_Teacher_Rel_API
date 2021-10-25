import pymysql.cursors
from dotenv import dotenv_values
import psycopg2.extras

config = dotenv_values(".env")

##################################################################################
##################################################################################

#mysql credentials

"""class DBConnection:
    conn = pymysql.connect(
        host=config.get('HOST'),
        user=config.get('USER'),
        password=config.get('PASSWORD'),
        db=config.get('DATABASE'),
        port=3308,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()

HOST=localhost
USER=root
PASSWORD=root
DATABASE=s_t
PORT=3308"""


##################################################################################
##################################################################################

#postgres credentials

class DBConnection:
    conn = psycopg2.connect(
        host=config.get('HOST'),
        database=config.get('DATABASE'),
        user=config.get('USER'),
        password=config.get('PASSWORD'),
        cursor_factory=psycopg2.extras.RealDictCursor
    )
    print("database connected")
    cursor = conn.cursor()