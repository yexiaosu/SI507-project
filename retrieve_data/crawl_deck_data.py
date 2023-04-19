import requests
from bs4 import BeautifulSoup
from cache import saveCache, openCache

CACHE_FILENAME = "retrieve_data/raw_data/decksMeta.json"

BASE_URL = 'https://www.hearthstonetopdecks.com/hearthstones-best-standard-ladder-decks/'

def main():
    ''' crawl top decks data from the website

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    decks = openCache(CACHE_FILENAME)
    if len(decks) == 0:
        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.find('div', class_='entry-content')
        decksListDivs = container.find_all('div', class_='td-content', recursive=True)
        decksListUrls = {}
        topDecks = []
        for decksListDiv in decksListDivs:
            a = decksListDiv.find('a')
            url = a['href']
            content = a.decode_contents()
            decksListUrls[content] = url
        for decksListUrlKey in decksListUrls:
            decks = getDecks(decksListUrls[decksListUrlKey])
            topDecks = topDecks + decks
        saveCache(topDecks, CACHE_FILENAME)


def getDecks(url):
    ''' crawl top decks data from the website

    Parameters
    ----------
    url: string
        the URL of the latest list of a type of decks

    Returns
    -------
    array
        a list of decks' meta information and code
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    decksParent = soup.find('table')
    decksContainers = decksParent.find_all('h4', recursive=True)
    decksDetailUrls = {}
    for decksContainer in decksContainers:
        a = decksContainer.find('a')
        url = a['href']
        content = a.decode_contents()
        decksDetailUrls[content] = url
    decks = []
    for decksDetailUrlKey in decksDetailUrls:
        deck = getDeck(decksDetailUrls[decksDetailUrlKey])
        decks.append(deck)
    return decks

def getDeck(url):
    ''' crawl deck data from the website

    Parameters
    ----------
    url: string
        the URL of the detail information of a deck

    Returns
    -------
    dictionary
        information of a deck
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    entryHeader = soup.find('header', class_='entry-header')
    deckMetaContainer = entryHeader.find('div', class_='deck-meta')
    deckMetaLinks = deckMetaContainer.find_all('a', recursive=True)
    deckMetaAll = [meta.decode_contents() for meta in deckMetaLinks]
    deck = {
        "class": deckMetaAll[0] if len(deckMetaAll) > 0 else "",
        "format": deckMetaAll[2] if len(deckMetaAll) > 2 else "",
        "type": deckMetaAll[3] if len(deckMetaAll) > 3 else "",
        "season": deckMetaAll[4] if len(deckMetaAll) > 4 else "",
        "style": deckMetaAll[5] if len(deckMetaAll) > 5 else "",
        "metaDeck": deckMetaAll[6] if len(deckMetaAll) > 6 else "",
    }
    deckCodeContainer = soup.find('button', class_='btn btn-dark btn-dark-tiny-wide')
    deckCode = deckCodeContainer.attrs["data-deck-code"]
    deck["code"] = deckCode
    return deck
    

if __name__ == '__main__':
    main()
