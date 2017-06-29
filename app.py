from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    data = [
            {'firstname': 'Ryan', 'lastname': 'Ermita', 'position': 'Software Engineer'},
            {'firstname': 'Reginald', 'lastname': 'Ventura', 'position': 'Frontend Engineer'},
            {'firstname': 'Chizuru', 'lastname': 'Iwashita', 'position': 'Admin Manager'},
            {'firstname': 'Lyle', 'lastname': 'Kaiklian', 'position': 'Creative Director'},
            {'firstname': 'Jezeniel', 'lastname': 'Zapanta', 'position': 'Lead Software Engineer'},
           ]

    response = {"data": data, "response_code": 200, "message": 'ok'}

    return jsonify(response)
