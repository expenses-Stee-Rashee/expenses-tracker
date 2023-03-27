from flask import Blueprint, render_template, request
import requests

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'POST':
        income = request.form['income']
        expense = request.form['expense']
        title = request.form['title']
        icon = request.form['icon']

        response = requests.post('https://localhost:7005/api/apicategory', data ={
            'income': income,
            'expense': expense,
            'title': title,
            'icon': icon
        })
        
        if response.ok:
            return 'Category Added'
        else: 
            return 'Failed to add category'

    else:    
        return render_template("categories.html")