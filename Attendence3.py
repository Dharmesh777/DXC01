def insert(Empcode, EmpName):
    import sqlite3
    con = sqlite3.connect('Attendence1.db')
    cur = con.cursor()
    Empcode = input("enter employee code :")
    EmpName = input("enter employee name :")
    cur.execute('''INSERT INTO Attendence1 (Empcode, EmpName) VALUES(?, ?)''', (Empcode, EmpName))
    con.commit()
    con.close()

def update(Empcode, date, entrytime):
    import sqlite3
    con = sqlite3.connect('Attendence1.db')
    cur = con.cursor()
    Empcode = input("Enter Employee code :")
    date = input("Enter date (dd/mm/yyyy) format : ")
    entrytime = input("Enter entery time : ")
    data = cur.execute('''UPDATE Attendence1 SET date = ?, entrytime = ?'''  ''' where Empcode = ?''', (date, entrytime, Empcode))
    con.commit()
    con.close()

def update1(Empcode,deptime):
    import sqlite3
    con = sqlite3.connect('Attendence1.db')
    cur = con.cursor()
    Empcode = input("Enter Employee code :")
    deptime = input("Enter departure time :")
    data = cur.execute('''UPDATE Attendence1 SET deptime = ?'''  ''' where Empcode = ?''', (deptime, Empcode))
    con.commit()
    con.close()

def fetch():
    import sqlite3
    con = sqlite3.connect('Attendence1.db')
    cur = con.cursor()
    data = cur.execute('''select * from Attendence1''')
    for row in data:
     Empcode = row[0]
     Empname = row[1]
     date = row[2]
     enterytime = row[3]
     deptime = row[4]

     print(str(Empcode) + " , " + Empname + " , " + str(date) + " , " + str(enterytime) + " , " + str(deptime))
    con.close()

choice = 9
while(choice != 0):
        print("Enter 1 for insert")
        print("enter 2 to update time and date ")
        print("enter 3 to update departure time ")
        print("enter 4 to fetcch all details ")
        print("")
        print("Enter 0 to EXIT")
        choice = int(input("Enter your choice :"))
        if choice == 1:
            print(insert('Empcode', 'EmpName'))
        elif choice == 2:
            print(update('Empcode', 'date', 'entrytime'))
        elif choice == 3:
            print(update1('Empcode', 'deptime'))
        elif choice == 4:
            print(fetch())