import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MSSQL\SQLEXPRESS;'
                      'Database=Winkars;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Winkars.dbo.user_information;')

f = open("data.txt", "w+")

for row in cursor.fetchall():
    row = list(row)
    f.write(str(row)+',\n')
