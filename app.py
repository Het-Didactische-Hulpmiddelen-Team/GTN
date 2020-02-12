from flask import Flask, render_template, request, json
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'dht'
app.config['MYSQL_PASSWORD'] = 'mvghetdhtmvghetdht'
app.config['MYSQL_DB'] = 'dht'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/add", methods=['POST'])
def add():
    _name = request.form['name']
    _url = request.form['url']
    cursor = mysql.connection.cursor()
    print(_url)
    print(_name)
    if _name and _url:
        cursor.execute("INSERT INTO gtn(name, url) VALUES (%s, %s)", (_name, _url))
        mysql.connection.commit()
        cursor.close()
        return render_template("success.html")
    return render_template("index.html")


@app.route("/overview")
def overview():
    return render_template('overview.html')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug = True)
