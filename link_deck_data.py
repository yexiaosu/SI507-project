import requests
import logging
import urllib.parse
from cache import saveCache, openCache
from oauth_token import getNewToken

CACHE_FILENAME = "./raw_data/decks.json"
DECK_META_FILE = "./raw_data/decksMeta.json"


def main():
    apiUrl = "https://us.api.blizzard.com/hearthstone/deck?locale=en_US"
    decks = openCache(CACHE_FILENAME)
    decksMeta = openCache(DECK_META_FILE)
    logging.captureWarnings(True)
    if len(decks) == 0:
        token = getNewToken()
        decks = []
        for deckMeta in decksMeta:
            deck = request(apiUrl, token, deckMeta["code"])
            deck["class"] = deckMeta["class"]
            deck["format"] = deckMeta["format"]
            deck["type"] = deckMeta["type"]
            deck["season"] = deckMeta["season"]
            deck["style"] = deckMeta["style"]
            deck["metaDeck"] = deckMeta["metaDeck"]
            decks.append(deck)
        saveCache(decks, CACHE_FILENAME)


def request(apiUrl, token, code):
    ''' make a request to the API and collect data of a deck

    Parameters
    ----------
    apiUrl: string
        URL of the deck API
    token: string
        OAuth 2.0 token
    code: string
        deck code of the deck

    Returns
    -------
    dictionary
        information of the deck
    '''
    code = urllib.parse.quote_plus(code)
    deck = {}
    requestUrl = apiUrl + f"&code={code}"
    apiHeaders = {'Authorization': 'Bearer ' + token}
    apiResponse = requests.get(requestUrl, headers=apiHeaders, verify=False)
    if apiResponse.status_code == 401:
        token = getNewToken()
    else:
        responseJson = apiResponse.json()
        deck["hero"] = responseJson["hero"]
        deck["heroPower"] = responseJson["heroPower"]
        deck["cards"] = responseJson["cards"]
    return deck


if __name__ == '__main__':
    main()
