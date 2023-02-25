from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
cnx = mysql.connector.connect(user='db_user', password='db_password', host='db_host', database='db_name')

# Define API endpoint to return users
@app.route('/users')
def get_users():
    cursor = cnx.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = []
    for (id, name, email) in cursor:
        user = {
            'id': id,
            'name': name,
            'email': email
        }
        users.append(user)
    cursor.close()
    return jsonify(users)

# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
