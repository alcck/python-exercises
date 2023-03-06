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

#insert(1,'capybara',100)
#insert(2,'duck',150)

def view():
    conn = psycopg2.connect("dbname='data2' user='postgres' password='nimda123*' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data2")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#print(view())

def delete(roll):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='nimda123*' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM data2 WHERE rollno=%s", (roll,))
    conn.commit()
    conn.close()


#delete(2)
#print(view())

def update(nam, mark, roll):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='nimda123*' port='5432' host='localhost' ")
    cur = conn.cursor()
    cur.execute("UPDATE data2 SET name=%s , marks=%s  WHERE rollno=%s", (nam, mark, roll))
    conn.commit()
    conn.close()

update('mouse', 200, 2)
print(view())