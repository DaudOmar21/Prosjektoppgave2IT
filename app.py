from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host = 'localhost',
    username = 'daud21',
    password = 'Daauud2008',
    database ='test'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
result = cursor.fetchall()

@app.route('/')
def index():
    return render_template('Kantine.html')



@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        passord = request.form['passord']
        cursor.execute('SELECT * FROM users WHERE username = %s AND passord = %s', (username, passord))

        if cursor.fetchone():
            return('Login successful')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')



@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        passord = request.form['passord']
        cursor.execute('INSERT INTO users (username, passord) VALUES (%s, %s)', (username, passord))
        conn.commit()
        return('Registration successful')
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)