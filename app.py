from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'dht'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mvghetdhtmvghetdht'
app.config['MYSQL_DATABASE_DB'] = 'dht'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/add", methods=['POST'])
def add():
    _name = request.form['name']
    _url = request.form['url']

    if _name and _url:
        cursor.callproc('sp_adduser', (_name, _url))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})

    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route("/overview")
def overview():
    return render_template('overview.html')

if __name__ == "__main__":
    app.run()
