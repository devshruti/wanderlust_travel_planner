from flask import Blueprint, jsonify, request
from app.models import Expense, db

expense_bp = Blueprint('expense_bp', __name__)

@expense_bp.route('/expenses', methods=['GET'])
def get_expenses():
    # Logic to retrieve expenses
    # Return expenses as JSON

@expense_bp.route('/expense/add', methods=['POST'])
def add_expense():
    data = request.get_json()
    new_expense = Expense(description=data['description'], amount=data['amount'], category=data['category'])
 
    # Logic to add an expense
    # Extract data from the request and store it in the database

@expense_bp.route('/expense/update/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense:
        data = request.get_json()
        expense.description = data.get('description', expense.description)
        expense.amount = data.get('amount', expense.amount)
        expense.category = data.get('category', expense.category) # Logic to update a specific expense
    # Extract updated data from the request and update the expense

@expense_bp.route('/expense/delete/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense:
        db.session.delete(expense)# Logic to delete a specific expense
    # Find and delete the expense from the database
