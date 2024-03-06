import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'makaveli@4199'


	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Post")

