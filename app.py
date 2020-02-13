import re
from flask import Flask, render_template, request, json, jsonify
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
    _url = re.sub(r'.*github', 'github', request.form['url'])

    if _name and _url:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO gtn(name, url) VALUES (%s, %s)", (_name, _url))
        mysql.connection.commit()
        cursor.close()
        return render_template("success.html")
    return render_template("index.html")


@app.route("/overview")
def overview():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM gtn order by name")
    users = cursor.fetchall()
    return render_template('overview.html', users=users)

@app.route("/name/<name>")
def get_name(name):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM gtn WHERE name like %s", ["%"+name+"%"])
    user = cursor.fetchall()
    return jsonify(user)

@app.route("/user/<username>")
def get_username(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM gtn WHERE url like %s", ["%"+username+"%"])
    user = cursor.fetchall()
    return jsonify(user)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug = True, port=80)
