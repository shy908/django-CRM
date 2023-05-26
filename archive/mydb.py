import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'innovative77',
)

cursorObject = dataBase.cursor()
#create a database

cursorObject.execute("CREATE DATABASE manue")
print("All Done!")