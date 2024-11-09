from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = '12345678'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'crud_db'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to submit form data and save it to MySQL
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'Data saved successfully!'})

# API endpoint to fetch all records from MySQL
@app.route('/get_users', methods=['GET'])
def get_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()

    return jsonify(users)

# API endpoint to update a record by id
@app.route('/update_user/<int:id>', methods=['PUT'])
def update_user(id):
    if request.is_json:
        data = request.get_json()  # Get the JSON data from the request body
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s, phone = %s WHERE id = %s", (name, email, phone, id))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'Data updated successfully!'})

# API endpoint to delete a record by id
@app.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'Data deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
