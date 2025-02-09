from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, Expense

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']
        new_expense = Expense(date=date, category=category, amount=amount, description=description)
        db.session.add(new_expense)
        db.session.commit()
        return redirect('/')
    return render_template('add_expense.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    if request.method == 'POST':
        expense.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        expense.category = request.form['category']
        expense.amount = float(request.form['amount'])
        expense.description = request.form['description']
        db.session.commit()
        return redirect('/')
    return render_template('edit_expense.html', expense=expense)

@app.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
