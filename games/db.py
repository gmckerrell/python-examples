"""
This module provides database utility functions for a games database
"""
import sqlite3
import hashlib
import datetime

from collections import namedtuple

def namedtuple_factory(cursor, row):
    """Returns sqlite rows as named tuples."""
    fields = [col[0] for col in cursor.description]
    Row = namedtuple("Row", fields)
    return Row(*row)

def initialise(conn):
    # create the tables in the database
    with conn:
        c = conn.cursor()
        c.executescript(
            """
            DROP TABLE IF EXISTS users;
            CREATE TABLE users (
                id                    INTEGER PRIMARY KEY AUTOINCREMENT,
                name                  TEXT                NOT NULL,
                password_hash         TEXT                NOT NULL,
                account_creation_date TEXT                NOT NULL
            );

            DROP TABLE IF EXISTS games;
            CREATE TABLE games (
                id   INTEGER PRIMARY KEY  AUTOINCREMENT,
                name TEXT    UNIQUE       NOT NULL
            );

            DROP TABLE IF EXISTS results;
            CREATE TABLE results (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                game_id    INTEGER             NOT NULL,
                player1_id INTEGER             NOT NULL,
                player2_id INTEGER             NOT NULL,
                score1     INTEGER             NOT NULL,
                score2     INTEGER             NOT NULL
            );
            """
        )

def get_users(conn):
    with conn:
        c = conn.cursor()
        c.row_factory = namedtuple_factory
        c.execute("SELECT * FROM users")
        return c.fetchall()

def get_user(conn, id):
    with conn:
        c = conn.cursor()
        c.row_factory = namedtuple_factory
        c.execute("SELECT * FROM users WHERE id = ?", [id])
        return c.fetchone()

def create_user(conn, name, password):
    with conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO users (name, password_hash, account_creation_date) VALUES(?,?,?)",
            [
                name,
                hashlib.sha256(
                    password.encode('utf-8')
                ).hexdigest(),
                datetime.date.today()
            ]
        )
        return c.lastrowid

def get_games(conn):
    with conn:
        c = conn.cursor()
        c.row_factory = namedtuple_factory
        c.execute("SELECT * FROM games")
        return c.fetchall()

def get_game(conn, id):
    with conn:
        c = conn.cursor()
        c.row_factory = namedtuple_factory
        c.execute("SELECT * FROM games WHERE id = ?", [id])
        return c.fetchone()
    
def create_game(conn, name):
    with conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO games (name) VALUES(?)",
            [name]
        )
        return c.lastrowid

def get_results(conn):
    with conn:
        c = conn.cursor()
        c.row_factory = namedtuple_factory
        c.execute("SELECT * FROM results")
        return c.fetchall()

def get_result(conn, id):
    with conn:
        c = conn.cursor()
        c.row_factory = namedtuple_factory
        c.execute("SELECT * FROM results WHERE id = ?", [id])
        return c.fetchone()

def create_result(conn, game_id, player1_id, player2_id, score1, score2):
    with conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO results (game_id, player1_id, player2_id, score1, score2) VALUES(?,?,?,?,?)",
            [game_id, player1_id, player2_id, score1, score2]
        )
        return c.lastrowid

def get_joinedresults(conn):
    with conn:
        c = conn.cursor()
        c.row_factory = namedtuple_factory
        c.execute(
            """
            SELECT
                games.name     AS game,
                users1.name    AS user1,
                users2.name    AS user2,
                results.score1 AS score1,
                results.score2 AS score2
            FROM results
            INNER JOIN games
                ON games.id = results.game_id
            INNER JOIN users AS users1
                ON users1.id = results.player1_id
            INNER JOIN users AS users2
                ON users2.id = results.player2_id
            """
        )
        return c.fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect("games.db")

    print("Initialising database")
    initialise(conn)

    alice_id   = create_user(conn, "Alice",   "password")
    bob_id     = create_user(conn, "Bob",     "changeme")
    charlie_id = create_user(conn, "Charlie", "hello")
    print("\nUSERS")
    for user in get_users(conn):
        print(user)

    chess_id    = create_game(conn, "Chess")
    draughts_id = create_game(conn, "Draughts")
    print("\nGAMES")
    for game in get_games(conn):
        print(game)

    create_result(conn, chess_id,    alice_id, bob_id,     2, 0)
    create_result(conn, chess_id,    alice_id, bob_id,     0, 2)
    create_result(conn, draughts_id, charlie_id, bob_id,   2, 0)
    create_result(conn, draughts_id, alice_id, bob_id,     1, 1)
    create_result(conn, draughts_id, alice_id, charlie_id, 0, 2)

    print("\nRESULTS")
    for result in get_results(conn):
        print(result)

    print("\nJOINED RESULTS")
    for result in get_joinedresults(conn):
        print(result)


    
    conn.close()
