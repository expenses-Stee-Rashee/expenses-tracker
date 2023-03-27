from flask import Flask
from views.home import home_bp
from views.transactions import transactions_bp
from views.newTransaction import newTransaction_bp
from views.categories import categories_bp



app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(newTransaction_bp)
app.register_blueprint(categories_bp)


if __name__ == "__main__":
    app.run(debug=True)
