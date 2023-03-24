from flask import Blueprint, render_template, request
import requests

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions', methods=['GET', 'POST'])
def transactions():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        note = request.form['note']

        response = requests.post('https://localhost:7005/api/transactionapi', data ={
            'date': date,
            'category': category,
            'amount': amount,
            'note': note
        })
        
        if response.ok:
            return 'Transaction Added'
        else: 
            return 'Failed to add transaction'

    else:    
        return render_template("transactions.html")

