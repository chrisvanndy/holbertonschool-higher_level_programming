#!/usr/bin/python3
"""Write a script that lists all states from the hbtn_0e_0_usa database"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    cursor = db.cursor()

    cursor.execute("""
        SELECT * FROM states
        WHERE name = BINARY "{}"
        """.format(argv[4]))

    states = cursor.fetchall()

    for state in states:
            print(state)
