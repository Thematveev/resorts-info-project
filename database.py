import sqlite3
import config

connection = sqlite3.connect(
    f"./{config.DATABASE_NAME}", check_same_thread=False)


def create_database():
    connection.execute(
        "CREATE TABLE IF NOT EXISTS users (id integer primary key autoincrement, email text unique, pass text);")
    connection.execute(
        "create table if not exists history  (id integer primary key autoincrement,user_id integer references users(id),search_text text not null);"
    )

def add_new_search(search_text, user_id):
    connection.execute(
        "insert into history(user_id, search_text) values (?, ?);",
        [user_id, search_text]
    )

    connection.commit()


def register_new_user(email, password):
    connection.execute(
        "INSERT INTO users(email, pass) VALUES (?, ?);", [email, password])
    connection.commit()


def check_login(email, password):
    result = connection.execute(
        "SELECT * FROM users WHERE email = ? AND pass = ?;", [email, password]).fetchone()
    return result

def get_id_by_email(email):
    result = connection.execute("select id from users where email = ?;", [email]).fetchone()[0]
    return result

def get_searches(email):
    results = connection.execute("select search_text from history join users on users.id = history.user_id where users.email = ? order by history.id desc limit 3;", [email]).fetchall()
    return [i[0] for i in results]

create_database()
