# gtn


## Github -> Name
Allows for easy translation between the real name of UCLL students and their Github usernames


## Usage
1. Install required modules listed in requirements.txt using `pip install -r requirements.txt`
1. Run the app using `python3 app.py`
  * Default port: 82
  * Endpoints: see below


## Endpoints
* */ [GET]*
  Form for students on which they fill in their names and usernames
  Sends a POST request to the */add [POST]* endpoint (see below)

* */add [POST]*
  Inserts the name and usernames into the local MySQL database *dht*, table *gtn*

* */overview [GET]*
  Lists all entries in the MySQL database

* */name/<real-name> [GET]*
  Returns name and username for a given `<real-name>`
  
* */user/<username> [GET]*
  Returns name and username for a given `<username>`


Made by the offical "Didactical Aids Team"
