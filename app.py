import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Initialize the SQLite database
def init_db():
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )''')
        conn.commit()

init_db()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('SELECT password FROM users WHERE email = ?', (email,))
        user = c.fetchone()

    if user and user[0] == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        try:
            c.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({"message": "User already exists"}), 400

    return jsonify({"message": "Signup successful"}), 201

@app.route('/tables', methods=['GET'])
def list_tables():
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
    return jsonify({"tables": [table[0] for table in tables]}), 200

@app.route('/table/<table_name>', methods=['GET'])
def view_table(table_name):
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        query = f"SELECT * FROM {table_name}"
        c.execute(query)
        results = c.fetchall()
        columns = [description[0] for description in c.description]
    return jsonify({"columns": columns, "data": results}), 200

if __name__ == '__main__':
    app.run(debug=True)
