import sqlite3

con = sqlite3.connect("Attendence2.db")

cur = con.cursor()

Table = """CREATE TABLE Attendence1 (Empcode int, EmpName VARCHAR(30), date int, entrytime , deptime );"""

cur.execute(Table)

con.commit()

con.close()