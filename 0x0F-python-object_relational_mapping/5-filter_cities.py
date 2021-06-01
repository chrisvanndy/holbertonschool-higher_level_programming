#!/usr/bin/python3
"""Write a script that lists all states from the hbtn_0e_0_usa database"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    cursor = db.cursor()

    cursor.execute("""
        SELECT
            cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name = BINARY %(name)s
        """, {
            'name': argv[4]
        })

    cities = cursor.fetchall()

    c_list = []
    for city in cities:
        c_list.append(city[0])
    print(", ".join(c_list))
