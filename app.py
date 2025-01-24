import datetime
from flask_bootstrap import Bootstrap4
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Enum

app = Flask(__name__)
bootstrap = Bootstrap4(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Expense(db.Model()):
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String(40))
    details = db.Column(db.String(80))
    amount_dolars = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Enum('pending', 'approved', 'declined', name='status_enum'), default='pending')

EXPENSES = [
    {
        "id": 1,
        "supplier": "Food",
        "details": "Team lunch",
        "us": 18.99,
        "date": "01/01/25",
        "status": "Approved",
    },
    {
        "id": 2,
        "supplier": "Uber",
        "details": "Team lunch",
        "us": 20.87,
        "date": "01/01/25",
        "status": "Declined",
    },
    {
        "id": 3,
        "supplier": "Udemy",
        "details": "Python Course",
        "us": 30.00,
        "date": "01/01/25",
        "status": "Pending",
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', expenses=EXPENSES)

@app.route("/api/expenses")
def list_expenses():
    return jsonify(EXPENSES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)