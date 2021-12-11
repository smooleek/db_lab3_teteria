import psycopg2
import csv

INPUT_CSV_FILE = 'amd_processors.csv'

query1 = '''
CREATE TABLE processors3
(
    processor_id integer,
    name character(20),
    product_line character(20),
    cores int,
    threads int,
    url character varying(100),
    CONSTRAINT pk_processors PRIMARY KEY (processor_id)
)
'''
query2 = '''
INSERT INTO processors3(processor_id, name, product_line, cores, threads, url) VALUES (1,2,3,4,5,6)
'''
connection = psycopg2.connect(user='postgres', password='postgres', dbname='testdb21', host='localhost', port='5432')
with connection:
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS processors3')
    cursor.execute(query1)
    cursor.execute(query2)

    with open(INPUT_CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for items, elements in enumerate(reader):
            values = (items, elements['processor_id'], items['name'], elements['product_line'], elements['threads'], elements['url'])
            cursor.execute(query1, values)
    connection.commit()