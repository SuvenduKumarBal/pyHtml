from flask import Flask, render_template, request, redirect, url_for, session, flash
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    'admin': {'password': 'adminpass', 'role': 'superadmin'},
    'user1': {'password': 'userpass', 'role': 'admin'}
}

dashboard_data = {
    'region1': {'booth1': {'voters': 100}, 'booth2': {'voters': 150}},
    'region2': {'booth3': {'voters': 120}, 'booth4': {'voters': 90}}
}

logging.basicConfig(filename='dashboard.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_activity(activity):
    logging.info(f"User '{session['username']}' performed: {activity}")

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username]['password'] == password:
        session['username'] = username
        session['role'] = users[username]['role']
        log_activity('login')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials', 'error')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        log_activity('accessed the dashboard')
        return render_template('dashboard.html', data=dashboard_data)
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    log_activity('logged out')
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
