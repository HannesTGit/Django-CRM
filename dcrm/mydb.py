import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '33hts7zZj4sEs600PEgz'
    
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")