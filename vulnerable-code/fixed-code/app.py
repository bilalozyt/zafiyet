from flask import Flask, request, render_template, g
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'users.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """Veritabanını örnek kullanıcılarla başlat"""
    if not os.path.exists(DATABASE):
        with app.app_context():
            db = get_db()
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    role TEXT NOT NULL
                )
            ''')
            
            users = [
                (1, 'admin', 'admin@example.com', 'yönetici'),
                (2, 'mehmet', 'mehmet@example.com', 'kullanıcı'),
                (3, 'ayşe', 'ayse@example.com', 'kullanıcı'),
                (4, 'ahmet', 'ahmet@example.com', 'moderatör'),
                (5, 'zeynep', 'zeynep@example.com', 'kullanıcı')
            ]
            cursor.executemany('INSERT INTO users VALUES (?, ?, ?, ?)', users)
            db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    username = request.form.get('username', '')
    
    db = get_db()
    cursor = db.cursor()
    
    query = "SELECT * FROM users WHERE username LIKE ?"
    search_pattern = f"%{username}%"
    
    try:
        cursor.execute(query, (search_pattern,))
        results = cursor.fetchall()
        return render_template('search_results.html', results=results, query=f"{query} parametresi: {search_pattern}")
    except Exception as e:
        return render_template('search_results.html', error=str(e), query=f"{query} parametresi: {search_pattern}")

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8000, debug=True)
