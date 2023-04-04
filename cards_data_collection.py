import sys
import requests
import json
import logging
from cache import saveCache, openCache
from oauthToken import getNewToken

CACHE_FILENAME = "cards.json"

def main():
    ''' get and save data of cards

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    apiUrl = "https://us.api.blizzard.com/hearthstone/cards?locale=en_US"
    cards = openCache(CACHE_FILENAME)
    if len(cards) == 0:
        cards = request(apiUrl)
        saveCache(cards, CACHE_FILENAME)


def request(apiUrl):
    ''' make a request to the API and collect data of cards

    Parameters
    ----------
    apiUrl: string
        URL of the card API

    Returns
    -------
    array
        array of cards
    '''
    logging.captureWarnings(True)

    token = getNewToken()
    page = 1
    cards = []
    while True:
        requestUrl = apiUrl + f"&page={page}"
        apiHeaders = {'Authorization': 'Bearer ' + token}
        apiResponse = requests.get(
            requestUrl, headers=apiHeaders, verify=False)
        if apiResponse.status_code == 401:
            token = getNewToken()
        else:
            responseJson = apiResponse.json()
            if responseJson["page"] > responseJson["pageCount"]:
                break
            cards = cards + responseJson["cards"]
            page = page + 1
    return cards


if __name__ == '__main__':
    main()
