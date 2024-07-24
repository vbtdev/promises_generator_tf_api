from flask import Flask, jsonify, render_template
import json
import random

app = Flask(__name__)

@app.route('/')
def index():
    with open('promessas.json', 'r', encoding='utf-8') as f:
        promises = json.load(f)
    random_promise = random.choice(promises)
    versiculo = random_promise.get('versiculo', '')
    localizacao = random_promise.get('localizacao', '')
    combined_message = f"{versiculo} {localizacao}"
    return render_template('index.html', promessa=combined_message)

@app.route('/promessas', methods=['GET'])
def get_random_promise():
    with open('promessas.json', 'r', encoding='utf-8') as f:
        promises = json.load(f)
    random_promise = random.choice(promises)
    return jsonify(random_promise)  # Retorna o JSON da promessa completa

if __name__ == '__main__':
    app.run(debug=True)
