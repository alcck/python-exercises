import psycopg2

def createtable():
    conn = psycopg2.connect("dbname='data2' user='postgres' password='nimda123*' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data2(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()
#createtable()
def insert(roll, nam, mark):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='nimda123*' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO data2 VALUES(%s,%s,%s)",(roll,nam,mark))
    conn.commit()
    conn.close()

insert(1,'capybara',100)
insert(2,'duck',150)