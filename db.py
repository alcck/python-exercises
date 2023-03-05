import psycopg2

def createtable():
    conn = psycopg2.connect("dbname='data' user='postgres' password='nimda123*' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()

createtable()