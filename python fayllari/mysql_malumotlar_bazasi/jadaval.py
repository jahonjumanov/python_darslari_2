import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jahon19940920",
    database="maktab"
)
#jadvallarni ko'rish
mycursor=mydb.cursor()
mycursor.execute(
    """creat table ismlar
    (id int autoincr
    """)