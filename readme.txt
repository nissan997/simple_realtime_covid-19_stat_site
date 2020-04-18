This is a simple website created using Flask framework to show realtime covid 19 stats from worldmeter api.

I used a PyMySQL script to setup mysql database for this website called setup_db.py found in the root directory of this repo.

Then I wrote anoher PyMySQL script to update the data in the database from the worldmeter api,the script is also in the root directory called 'db_updater.py'.

Then I wrote a cronjob script to run the updater script every 10 minutes.
To add the crontab we have to run "crontab -e" in our terminal and add the following line in the crontab file,

*/2 * * * * python /your_local_directory/db_updater.py

remember to change your_local_directory to complete path of the file you kept the project.

Also in every python script change the db_username and db_password to your database username and password.
