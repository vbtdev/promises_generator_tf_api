from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

@app.route('/promessas', methods=['GET'])
def get_random_promise():
    with open('promessas.json', 'r', encoding='utf-8') as f:
        promises = json.load(f)
    random_promise = random.choice(promises)
    return jsonify({'promessa': random_promise})


if __name__ == '__main__':
    app.run()