from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
expenses = []

users = {
    'admin@example.com': 'password',
    'abhimakulshrestha2004@example.com': '1234',
    'user2@example.com': 'abc123'
}

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/expenses')
def expense_list():
    return render_template('expenses.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']
    expenses.append({'date': date, 'description': description, 'amount': amount})
    return redirect(url_for('expense_list'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Dummy credentials - replace with real user verification
        if username == 'user@gmail.com' and password == 'password':
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)

@app.route('/register')
def register():
    return render_template('register.html')
    

if __name__ == '__main__':
    app.run(debug=True)
