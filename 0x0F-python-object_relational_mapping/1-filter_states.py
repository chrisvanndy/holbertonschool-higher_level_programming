#!/usr/bin/python3
"""Write a script that lists all states from the hbtn_0e_0_usa database"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")

    states = cursor.fetchall()

    for state in states:
        if state[1].startswith("N"):
            print(state)
