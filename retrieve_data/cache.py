import json


def openCache(name):
    ''' opens the cache file if it exists and loads the JSON into the cache list.
    if the cache file doesn't exist, creates a new cache list

    Parameters
    ----------
    name: string
        cache file name

    Returns
    -------
    The opened cache
    '''
    try:
        cacheFile = open(name, 'r')
        cacheContents = cacheFile.read()
        cache = json.loads(cacheContents)
        cacheFile.close()
    except:
        cache = []
    return cache


def saveCache(cache, name):
    ''' saves the current state of the cache to disk

    Parameters
    ----------
    cache: list
        The list to save
    name: string
        cache file name

    Returns
    -------
    None
    '''
    dumpedJson = json.dumps(cache)
    fw = open(name, "w")
    fw.write(dumpedJson)
    fw.close()
