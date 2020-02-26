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

# ================================
# index endpoint returns index.html form
# ================================
@app.route("/")
def main():
    return render_template('index.html')


# ================================
# add endpoint returns success.html when adding was successful
# else the index.html form
# ================================
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

# ================================
# overview endpoint returns overview.html
# containing all entries in database (real name, github username)
# ================================
@app.route("/overview")
def overview():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM gtn order by name")
    users = cursor.fetchall()
    return render_template('overview.html', users=users)

# ================================
# get_name endpoint returns json
# containing the name and github username for a given name
# ================================
@app.route("/name/<name>")
def get_name(name):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM gtn WHERE name like %s", ["%"+name+"%"])
    user = cursor.fetchall()
    return jsonify(user)

# ================================
# get_username endpoint returns json
# containing the name and github username for a given username
# ================================
@app.route("/user/<username>")
def get_username(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM gtn WHERE url regexp %s", ["github.com/"+username+"$"])
    user = cursor.fetchall()
    return jsonify(user)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug = True, port=80)
