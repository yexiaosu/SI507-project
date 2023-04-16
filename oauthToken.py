import sys
import requests
import json

def readClient():
    file = open('client.txt', 'r')
    id = file.readline()
    secret = file.readline()
    file.close()
    return id, secret

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
    clientId, clientSecret = readClient()

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