from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/v1/recognition/<type>')
def hello( type ):
    return jsonify({"recognition_type" : type}), 200

