from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    other_name = request.form.get('other_name', '')
    matric_number = request.form['matric_number']
    school = request.form['school']
    department = request.form['department']
    course = request.form['course']

    # Insert data into the database
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO students (first_name, last_name, other_name, matric_number, school, department, course)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, other_name, matric_number, school, department, course))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/students')
def students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)

