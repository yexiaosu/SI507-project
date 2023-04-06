import requests
import logging
from cache import saveCache, openCache
from oauthToken import getNewToken

CACHE_FILENAME = "metaInfo.json"

def main():
    ''' get and save meta data

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    apiUrl = "https://us.api.blizzard.com/hearthstone/metadata?locale=en_US"
    meta = openCache(CACHE_FILENAME)
    if len(meta) == 0:
        meta = request(apiUrl)
        saveCache(meta, CACHE_FILENAME)


def request(apiUrl):
    ''' make a request to the API and collect meta data

    Parameters
    ----------
    apiUrl: string
        URL of the card API

    Returns
    -------
    dictionary
        meta data
    '''
    logging.captureWarnings(True)

    token = getNewToken()
    meta = {}
    apiHeaders = {'Authorization': 'Bearer ' + token}
    apiResponse = requests.get(apiUrl, headers=apiHeaders, verify=False)
    if apiResponse.status_code == 401:
        token = getNewToken()
    else:
        responseJson = apiResponse.json()
        meta["sets"] = [{
            element["id"]: element["name"],
        } for element in responseJson["sets"]]
        meta["types"] = [{
            element["id"]: element["name"],
        } for element in responseJson["types"]]
        meta["rarity"] = [{
            element["id"]: element["name"],
        } for element in responseJson["rarities"]]
        meta["class"] = [{
            element["id"]: element["name"],
        } for element in responseJson["classes"]]
        meta["keywords"] = [{
            element["id"]: element["name"],
        } for element in responseJson["keywords"]]
    return meta

if __name__ == '__main__':
    main()