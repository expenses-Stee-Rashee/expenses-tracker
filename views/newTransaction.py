from flask import Blueprint, render_template, request
import requests
import json

newTransaction_bp = Blueprint('newTransaction', __name__)

@newTransaction_bp.route('/newtransaction', methods=['GET', 'POST'])
def new_transaction():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        note = request.form['note']

        data = {
            'date': date,
            'category': category,
            'amount': amount,
            'note': note
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://localhost:7005/api/transactionapi', json=data, headers=headers)
        
        
        if response.ok:
            return 'Transaction Added'
        else: 
            return 'Failed to add transaction'

    else:    
        return render_template("newTransaction.html")
