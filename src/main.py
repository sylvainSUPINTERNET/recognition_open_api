from flask import Flask, jsonify

from src.recognition.recognition import process

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message" : "Welcome"}), 200



@app.route('/api/v1/recognition/<type>')
def recognition( type ):
    process(type)
    return jsonify({"recognition_type" : type}), 200

