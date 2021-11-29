import requests
import pandas as pd
import os


def checkTokenURI(contract_address):
    endpoint = "https://api.etherscan.io/api"
    params = {
        'module': 'contract',
        'action': 'getabi',
        'address': contract_address,
        'apikey': os.getenv('ETHERSCAN_APIKEY')
    }
    r = requests.get(endpoint, params=params)

    df = pd.read_json(r.json()['result'])

    return df