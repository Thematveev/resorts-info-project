import sqlite3
import config

connection = sqlite3.connect(
    f"./{config.DATABASE_NAME}", check_same_thread=False)


def create_database():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS users (id integer primary key autoincrement, email text unique, pass text);")


def register_new_user(email, password):
    connection.execute(
        "INSERT INTO users(email, pass) VALUES (?, ?);", [email, password])
    connection.commit()


def check_login(email, password):
    result = connection.execute(
        "SELECT * FROM users WHERE email = ? AND pass = ?;", [email, password]).fetchone()
    return result


create_database()
