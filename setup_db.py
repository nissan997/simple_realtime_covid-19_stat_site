import pymysql.cursors

connection = pymysql.connect(host='localhost',
							 user='#your_db_username',
							 password='#your_db_password')
try:
	with connection.cursor() as cursor:
		cursor.execute("DROP DATABASE IF EXISTS COVID_DATA")
		cursor.execute("CREATE DATABASE COVID_DATA")
		cursor.execute("USE COVID_DATA")
		cursor.execute("CREATE TABLE live_update (entry_id INT AUTO_INCREMENT,country CHAR(20) NOT NULL,active_cases INT,total_recovered INT,new_cases INT,total_cases INT,total_deaths INT,critical INT,new_deaths INT,cases_per_1M INT,somoy CHAR(20),PRIMARY KEY(entry_id))")

finally:
	connection.close()