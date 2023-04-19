import requests
import logging
from cache import saveCache, openCache
from oauth_token import getNewToken

CACHE_FILENAME = "retrieve_data/raw_data/metaInfo.json"

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
        meta["sets"] = appendData("sets", responseJson)
        meta["types"] = appendData("types", responseJson)
        meta["rarity"] = appendData("rarities", responseJson)
        meta["class"] = appendData("classes", responseJson)
        meta["keywords"] = appendData("keywords", responseJson)
    return meta

def appendData(key, rawData):
    data = {}
    for element in rawData[key]:
        data[element["id"]] = element["name"]
    return data

if __name__ == '__main__':
    main()