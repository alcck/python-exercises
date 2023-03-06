import sqlite3


def createtable():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()


# createtable()

def insert(roll, nam, mark):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)", (roll, nam, mark))
    conn.commit()
    conn.close()


# insert(1,'capybara',100)
# insert(2,'duck',150)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(roll):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=?", (roll,))
    conn.commit()
    conn.close()


# delete()

def update(nam, mark, roll):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=? , marks=?  WHERE rollno=?", (nam, mark, roll))
    conn.commit()
    conn.close()


update('mouse', 200, 2)
print(view())
