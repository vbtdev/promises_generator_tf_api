from flask import Flask, jsonify, render_template
import json
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    with open('promessas.json', 'r', encoding='utf-8') as f:
        promises = json.load(f)
    random_promise = random.choice(promises)
    versiculo = random_promise.get('versiculo', '')
    localizacao = random_promise.get('localizacao', '')
    combined_message = f"{versiculo} {localizacao}"

    # Seleciona uma imagem aleatória da pasta static/img
    img_folder = os.path.join(app.static_folder, 'img')
    img_files = os.listdir(img_folder)
    random_img = random.choice(img_files)

    return render_template('index.html', promessa=combined_message, imagem_fundo=random_img)

@app.route('/promessas', methods=['GET'])
def get_random_promise():
    with open('promessas.json', 'r', encoding='utf-8') as f:
        promises = json.load(f)
    random_promise = random.choice(promises)
    return jsonify(random_promise)

if __name__ == '__main__':
    app.run()
