import requests
import pandas as pd


def checkTokenURI(contract_address):
    endpoint = "https://api.etherscan.io/api"
    params = {
        'module': 'contract',
        'action': 'getabi',
        'address': contract_address,
        'apikey': 'XABY2ZXGJIC771B9ACVIVARRRU2MRY1UPE'
    }
    r = requests.get(endpoint, params=params)

    df = pd.read_json(r.json()['result'])

    return df