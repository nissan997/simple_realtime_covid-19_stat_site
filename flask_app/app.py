from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = '#your_db_name'
app.config['MYSQL_PASSWORD'] = '#your_db_password'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'COVID_DATA'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM live_update WHERE entry_id=(SELECT MAX(entry_id) FROM live_update)")
    result = cur.fetchall()
    export = result[0]
    return render_template('Index.html',query=export)
if __name__=="__main__":
    app.run(debug=True)