from flask import Flask, render_template, url_for, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decks')
def find_decks():
    formats = ["wild", "hydra", "mammoth", "classic"]
    classes = ["Warrior", "Warlock", "Shaman", "Rogue", "Priest", "Paladin", "Mage", "Hunter", "Druid", "Demon Hunter", "Death Knight"]
    return render_template('search_decks.html', formats = formats, classes = classes)

@app.route('/decks/<formats>/<classes>')
def show_decks(formats, classes):
    with open('data/decks_tree.json') as json_file:
        decks = json.load(json_file)
    print(decks)
    selected_decks = []
    if formats == "all":
        for format in decks:
            if classes == "all":
                for class_name in decks[format]:
                    selected_decks.extend(decks[format][class_name])
            else:
                selected_decks.extend(decks[format][classes])
    else:
        if classes == "all":
            for class_name in decks[formats]:
                selected_decks.extend(decks[formats][class_name])
        else:
            selected_decks.extend(decks[formats][classes])
    return render_template('decks.html', decks=selected_decks)

@app.route('/cards_data')
def get_cards_data():
    with open('data/cards_tree.json') as json_file:
        cards = json.load(json_file)
    return jsonify(cards)

@app.route('/decks_data')
def get_decks_data():
    with open('data/decks_tree.json') as json_file:
        decks = json.load(json_file)
    return jsonify(decks)


if __name__ == '__main__':
    app.run(debug=True)