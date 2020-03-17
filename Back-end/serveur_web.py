#!flask/bin/python
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import main

app = Flask(__name__)
CORS(app)


@app.route('/update_products', methods=['GET'])
def get_tasks():
    response=main.update_products()
    return jsonify({'value': response})

if __name__ == '__main__':
    app.run(debug=True, port='5000')
