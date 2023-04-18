from cache import saveCache, openCache

CARDS_FILENAME = "./raw_data/cards.json"
DECKS_FILENAME = "./raw_data/decks.json"
META_FILENAME = "./raw_data/metaInfo.json"

CARDSTREE_FILENAME = "./data/cards_tree.json"
DECKSTREE_FILENAME = "./data/decks_tree.json"

idToClass = {}
idToType = {}
idToRarity = {}
idToSet = {}
idToKeyword = {}


def main():
    cards = openCache(CARDS_FILENAME)
    decks = openCache(DECKS_FILENAME)
    meta = openCache(META_FILENAME)
    decks_tree = openCache(DECKSTREE_FILENAME)
    fillMeta(meta)
    if len(decks_tree) == 0:
        decks_tree = organizeDecks(decks)
        saveCache(decks_tree, DECKSTREE_FILENAME)
    cards_tree = openCache(CARDSTREE_FILENAME)
    if len(cards_tree) == 0:
        cards_tree = organizeCards(cards, decks)
        saveCache(cards_tree, CARDSTREE_FILENAME)
   


def fillMeta(meta):
    global idToClass, idToType, idToRarity, idToSet, idToKeyword
    idToClass = meta["class"]
    idToType = meta["types"]
    idToRarity = meta["rarity"]
    idToSet = meta["sets"]
    idToKeyword = meta["keywords"]



def organizeDecks(decks):
    decks_tree = {
        "wild": {
            "Warrior": [],
            "Warlock": [],
            "Shaman": [],
            "Rogue": [],
            "Priest": [],
            "Paladin": [],
            "Mage": [],
            "Hunter": [],
            "Druid": [],
            "Demon Hunter": [],
            "Death Knight": []
        },
        "hydra": {
            "Warrior": [],
            "Warlock": [],
            "Shaman": [],
            "Rogue": [],
            "Priest": [],
            "Paladin": [],
            "Mage": [],
            "Hunter": [],
            "Druid": [],
            "Demon Hunter": [],
            "Death Knight": []
        },
        "mammoth": {
            "Warrior": [],
            "Warlock": [],
            "Shaman": [],
            "Rogue": [],
            "Priest": [],
            "Paladin": [],
            "Mage": [],
            "Hunter": [],
            "Druid": [],
            "Demon Hunter": [],
            "Death Knight": []
        },
        "wolf": {
            "Warrior": [],
            "Warlock": [],
            "Shaman": [],
            "Rogue": [],
            "Priest": [],
            "Paladin": [],
            "Mage": [],
            "Hunter": [],
            "Druid": [],
            "Demon Hunter": [],
            "Death Knight": []
        },
        "classic": {
            "Warrior": [],
            "Warlock": [],
            "Shaman": [],
            "Rogue": [],
            "Priest": [],
            "Paladin": [],
            "Mage": [],
            "Hunter": [],
            "Druid": [],
            "Demon Hunter": [],
            "Death Knight": []
        }
    }
    id = 0
    for deck in decks:
        if not deck["season"].startswith('season'):
            continue
        decks_tree[deck["format"]][deck["class"]].append({
            "id": id,
            "format": deck["format"],
            "class": deck["class"],
            "type": deck["type"],
            "season": deck["season"],
            "style": deck["style"],
            "metaDeck": deck["metaDeck"],
            "hero": {
                "name": deck["hero"]["name"],
                "class": idToClass[str(deck["hero"]["classId"])],
                "image": deck["hero"]["image"]
            },
            "heroPower": {
                "name": deck["heroPower"]["name"],
                "text": deck["heroPower"]["text"],
                "image": deck["heroPower"]["image"]
            },
            "cards": [{
                "id": card["id"],
                "class": idToClass[str(card["classId"])],
                "cardType": idToType[str(card["cardTypeId"])],
                "cardSet": idToSet[str(card["cardSetId"])] if card["cardSetId"] != 3 and card["cardSetId"] != 4 else idToSet["1635"],
                "rarity": idToRarity[str(card["rarityId"])],
                "manaCost": card["manaCost"],
                "name": card["name"],
                "text": card["text"],
                "image": card["image"],
                "cropImage": card["cropImage"],
                "keywords": [idToKeyword[str(id)] for id in card["keywordIds"] if str(id) in idToKeyword] if "keywordIds" in card else []
            } for card in deck["cards"]]
        })
        id = id + 1
    return decks_tree

def organizeCards(cards, decks):
    cards_tree = {
        "Warrior": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Warlock": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Shaman": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Rogue": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Priest": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Paladin": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Mage": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Hunter": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Druid": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Demon Hunter": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Death Knight": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        },
        "Neutral": {
            "Hero": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Minion": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Spell": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Weapon": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "HeroPower": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Location": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            },
            "Reward": {
                "Common": [],
                "Free": [],
                "Rare": [],
                "Epic": [],
                "Legendary": []
            }
        }
    }
    idCards = {}
    for card in cards:
        idCards[card["id"]] = card
        idCards[card["id"]]["popular"] = 0
    
    for deck in decks:
        for card in deck["cards"]:
            idCards[card["id"]]["popular"] += 1

    for id in idCards:
        card = idCards[id]
        if card["cardSetId"] == 17:   # skin
            continue
        cards_tree[idToClass[str(card["classId"])]][idToType[str(card["cardTypeId"])]][idToRarity[str(card["rarityId"])]].append({
            "id": card["id"],
            "class": idToClass[str(card["classId"])],
            "cardType": idToType[str(card["cardTypeId"])],
            "cardSet": idToSet[str(card["cardSetId"])] if card["cardSetId"] != 3 and card["cardSetId"] != 4 else idToSet["1635"],
            "rarity": idToRarity[str(card["rarityId"])],
            "manaCost": card["manaCost"],
            "name": card["name"],
            "text": card["text"],
            "flavorText": card["flavorText"],
            "artistName": card["artistName"],
            "image": card["image"],
            "cropImage": card["cropImage"],
            "keywords": [idToKeyword[str(id)] for id in card["keywordIds"] if str(id) in idToKeyword] if "keywordIds" in card else [],
            "popular": card["popular"]
        })
    return cards_tree


if __name__ == '__main__':
    main()
