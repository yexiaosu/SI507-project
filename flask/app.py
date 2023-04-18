from flask import Flask, render_template, url_for, jsonify
import json
from operator import itemgetter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decks')
def find_decks():
    formats = ["wild", "wolf", "hydra", "mammoth", "classic"]
    classes = ["Warrior", "Warlock", "Shaman", "Rogue", "Priest", "Paladin", "Mage", "Hunter", "Druid", "Demon Hunter", "Death Knight"]
    return render_template('search_decks.html', formats = formats, classes = classes)

@app.route('/decks/<formats>/<classes>')
def show_decks(formats, classes):
    with open('data/decks_tree.json') as json_file:
        decks = json.load(json_file)
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
    return render_template('decks.html', decks=selected_decks, format=formats, class_name=classes)

@app.route('/decks/<formats>/<classes>/<deck_id>')
def deck_detail(formats, classes, deck_id):
    with open('data/decks_tree.json') as json_file:
        decks = json.load(json_file)
    selected_deck = None
    for format in decks:
        if format != formats:
            continue
        for class_name in decks[format]:
            if class_name != classes:
                continue
            for deck in decks[format][classes]:
                if deck["id"] == int(deck_id):
                    selected_deck = deck
    return render_template('deck_detail.html', deck=selected_deck)

@app.route('/cards')
def find_cards():
    classes = ["Warrior", "Warlock", "Shaman", "Rogue", "Priest", "Paladin", "Mage", "Hunter", "Druid", "Demon Hunter", "Death Knight", "Neutral"]
    types = ["Hero", "Minion", "Spell", "Weapon", "HeroPower", "Location", "Reward"]
    rarities = ["Common", "Free", "Rare", "Epic", "Legendary"]
    return render_template('search_cards.html', classes = classes, types = types, rarities = rarities)

@app.route('/cards/<classes>/<types>/<rarities>')
def show_cards(classes, types, rarities):
    with open('data/cards_tree.json') as json_file:
        cards = json.load(json_file)
    selected_cards = []
    if classes == "all":
        for class_name in cards:
            if types == "all":
                for type in cards[class_name]:
                    if rarities == "all":
                        for rarity in cards[class_name][type]:
                            selected_cards.extend(cards[class_name][type][rarity])
                    else:
                        selected_cards.extend(cards[class_name][type][rarities])
            else:
                if rarities == "all":
                    for rarity in cards[class_name][type]:
                        selected_cards.extend(cards[class_name][type][rarity])
                else:
                    selected_cards.extend(cards[class_name][type][rarities])
    else:
        if types == "all":
            for type in cards[classes]:
                if rarities == "all":
                    for rarity in cards[classes][type]:
                        selected_cards.extend(cards[classes][type][rarity])
                else:
                    selected_cards.extend(cards[classes][type][rarities])
        else:
            if rarities == "all":
                for rarity in cards[classes][type]:
                    selected_cards.extend(cards[classes][type][rarity])
            else:
                selected_cards.extend(cards[classes][type][rarities])
    selected_cards_sorted = sorted(selected_cards, key=itemgetter('popular'), reverse=True)
    return render_template('cards.html', cards=selected_cards_sorted, class_name = classes, type = types, rarity = rarities)

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
    app.run(port=8000, debug=True)