#!/usr/bin/python3
"""Write a script that lists all states from the hbtn_0e_0_usa database"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    cursor = db.cursor()

    cursor.execute("""
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        """)

    cities = cursor.fetchall()

    for city in cities:
            print(city)
