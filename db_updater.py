from worldmeter.coronavirus import CovidMeter
import pymysql.cursors

c = CovidMeter()

data = c.global_data()

desh = data["country"]
bortoman_cases = data["active_cases"]
mot_recovered = data["total_recovered"]
notun_cases = data["new_cases"]
mot_cases = data["total_cases"]
mot_deaths = data["total_deaths"]
kharap = data["critical"]
notun_deaths = data["new_deaths"]
cases_proti_1M = data["cases_per_1M"]
somoy = data["date"]

connection = pymysql.connect(host='localhost',
							 user='#your_db_user_name',
							 password='#your_db_password')
try:
	with connection.cursor() as cursor:
		cursor.execute("USE COVID_DATA")
		insert = "INSERT INTO live_update(country,active_cases,total_recovered,new_cases,total_cases,total_deaths,critical,new_deaths,cases_per_1M,somoy) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		cursor.execute(insert,(desh,bortoman_cases,mot_recovered,notun_cases,mot_cases,mot_deaths,kharap,notun_deaths,cases_proti_1M,somoy))
		connection.commit()
		
finally:
	connection.close()

