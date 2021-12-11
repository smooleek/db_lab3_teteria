import psycopg2
import json

jsonconn = {}
tabnames = ['Processors', 'Info', 'Specifications']
connection = psycopg2.connect(user='postgres', password='postgres', dbname='testdb21', host='localhost', port='5432')
with connection:
    cursor = connection.cursor()
    for item in tabnames:
        cursor.execute('SELECT * FROM ' + item)
        rows = []
        for el in cursor.description:
            f = el[0]

        for row in cursor:
            rows.append(dict(zip(f, row)))

        jsonconn[item] = rows

    with open('processors.json', 'w') as outf:
        json.dump(jsonconn, outf, default=str)