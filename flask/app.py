from flask import Flask, render_template, url_for, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cards_data')
def get_data():
    with open('data/cards_tree.json') as json_file:
        cards = json.load(json_file)
    return jsonify(cards)


if __name__ == '__main__':
    app.run(debug=True)