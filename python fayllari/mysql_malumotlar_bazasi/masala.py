import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jahon19940920",
    database="maktab"
)
#jadvallarni ko'rish
mycursor=mydb.cursor()
mycursor.execute("show tables")
for db in mycursor:
    print(db)
def jasdval_korish(cursor):
    cursor.execute("select * from uqituvchilar")
    for i in cursor:
        print(i)
jasdval_korish(mycursor)


