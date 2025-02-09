from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Expense Model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)

# Home Route - Display Expenses with Filters
@app.route('/')
def index():
    category = request.args.get('category', '')
    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    min_amount = request.args.get('min_amount', '')
    max_amount = request.args.get('max_amount', '')

    query = Expense.query

    # Apply filters
    if category:
        query = query.filter_by(category=category)
    if start_date:
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        query = query.filter(Expense.date >= start_date_obj)
    if end_date:
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        query = query.filter(Expense.date <= end_date_obj)
    if min_amount:
        query = query.filter(Expense.amount >= float(min_amount))
    if max_amount:
        query = query.filter(Expense.amount <= float(max_amount))

    expenses = query.order_by(Expense.date.desc()).all()

    # Calculate Total Amount Spent
    total_spent = sum(expense.amount for expense in expenses)

    return render_template('index.html', expenses=expenses, total_spent=total_spent)

# Add Expense Route
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']

        new_expense = Expense(
            date=datetime.strptime(date, '%Y-%m-%d'),
            category=category,
            amount=amount,
            description=description
        )

        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_expense.html')

# Edit Expense Route
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':
        expense.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        expense.category = request.form['category']
        expense.amount = float(request.form['amount'])
        expense.description = request.form['description']

        db.session.commit()
        flash('Expense updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('edit_expense.html', expense=expense)

# Delete Expense Route
@app.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully!', 'danger')
    return redirect(url_for('index'))

# Run App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
