import psycopg2
import matplotlib.pyplot as plt

query1 = '''
CREATE VIEW ProcessorCores AS SELECT name, cores FROM Specifications INNER JOIN Processors ON Processors.Processor_id = Specifications.Processor_id
'''

query2 = '''
CREATE VIEW ProductLineQuantity AS SELECT DISTINCT product_line, count(*) FROM Processors GROUP BY Processors.Product_line
'''
query3 = '''
CREATE VIEW BoxedSpecifications AS SELECT name, cores, threads from Specifications INNER JOIN info ON info.info = specifications. processor_id INNER JOIN Processors ON Processors.processor_id = specifications. processor_id WHERE vertical_segment = 'Boxed Processor'
'''

connection = psycopg2.connect(user='postgres', password='postgres', dbname='testdb21', host='localhost', port='5432')
with connection:
    cursor = connection.cursor()

    print('Query 1:')
    cursor.execute('DROP VIEW IF EXISTS ProcessorCores')
    cursor.execute(query1)
    cursor.execute('SELECT * FROM ProcessorCores')
    name = []
    values = []
    for item in cursor:
        print(item)
        name.append(item[0])
        values.append(item[1])

    fig1 = plt.bar(name, values,width = 0.7)

    print("Query 2:")
    cursor.execute('DROP VIEW IF EXISTS ProductLineQuantity')
    cursor.execute(query2)
    cursor.execute('SELECT * FROM ProductLineQuantity')
    product_line = []
    count = []

    for item in cursor:
        print(item)
        product_line.append(item[0])
        count.append(item[1])

    fig2, ax = plt.subplots()
    ax.pie(count, labels=product_line)
    ax.axis("equal")

    print('Query 3:')
    cursor.execute('DROP VIEW IF EXISTS BoxedSpecifications')
    cursor.execute(query1)
    cursor.execute('SELECT * FROM BoxedSpecifications')
    names = []
    cores = []
    threads = []
    for item in cursor:
        print(item)
        name.append(item[0])
        cores.append(item[1])
        threads.append(item[2])

    fig3 = plt.bar(names, cores, threads)

plt.show()