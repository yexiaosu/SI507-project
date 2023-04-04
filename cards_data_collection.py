import sys
import requests
import json
import logging
from cache import saveCache, openCache

CACHE_FILENAME = "cards.json"

def getNewToken():
    ''' get a new OAuth 2.0 token from the authentication server

    Parameters
    ----------
    None

    Returns
    -------
    string
        the token
    '''
    authServerUrl = "https://oauth.battle.net/token"
    clientId = '2d49b07cd937443ca11518271989ed4d'
    clientSecret = 'cLeBHmV1yQPK9i6g8g13Iq5fxq6drTIT'

    tokenReqPayload = {'grant_type': 'client_credentials'}

    tokenResponse = requests.post(authServerUrl,
                                  data=tokenReqPayload, verify=False, allow_redirects=False,
                                  auth=(clientId, clientSecret))

    if tokenResponse.status_code != 200:
        print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)
    print("Successfuly obtained a new token")
    tokens = json.loads(tokenResponse.text)
    return tokens['access_token']


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
    None

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
