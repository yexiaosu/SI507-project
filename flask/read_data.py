import json

def load_decks_tree():
    ''' load decks tree

    Parameters
    ----------
    None

    Returns
    -------
    dictionary
        decks tree, with the structure of:
            root
            |- format
                |- class
                    |- list of decks
    '''
    with open('retrieve_data/data/decks_tree.json') as json_file:
        decks = json.load(json_file)
    return decks

def load_cards_tree():
    ''' load cards tree

    Parameters
    ----------
    None

    Returns
    -------
    dictionary
        cards tree, with the structure of:
            root
            |- class
                |- type
                    |- rarity
                        |- list of decks
    '''
    with open('retrieve_data/data/cards_tree.json') as json_file:
        cards = json.load(json_file)
    return cards