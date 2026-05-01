from flask import Flask, jsonify, render_template, request, redirect
import json
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection
MONGO_URI = "mongodb+srv://surajadmin:<Suraj12345>@cluster0.0ojwjfz.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["student_database"]
collection = db["students"]

# API Route
@app.route('/api')
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

# Form Page
@app.route('/')
def form():
    return render_template("form.html")

# Form Submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect('/success')

    except Exception as e:
        return f"Error: {str(e)}"

# Success Page
@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)

    @app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    try:
        item_name = request.form['itemName']
        item_description = request.form['itemDescription']

        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description
        })

        return "To-Do Item Submitted Successfully"

    except Exception as e:
        return f"Error: {str(e)}"