from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# route to home page
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        note = request.form['note']

        response = requests.post('https://api.example.com/transactions', data ={
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


if __name__ == "__main__":
    app.run(debug=True)