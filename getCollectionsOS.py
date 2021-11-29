import requests
import pandas as pd
import numpy as np


collections = open('collections-list.txt', 'r')
collection_report = []


def getCollectionStats(collection):
    endpoint = 'https://api.opensea.io/api/v1/collection/'

    response = requests.get(url=endpoint+collection)
    data = response.json()

    return data


def parseCollectionDetails(data):
    details = {
        'name': data['collection']['primary_asset_contracts'][0]['name'],
        'slug': data['collection']['slug'],
        'symbol': data['collection']['primary_asset_contracts'][0]['symbol'],
        'contract_address': data['collection']['primary_asset_contracts'][0]['address'],
        'payout_address': data['collection']['primary_asset_contracts'][0]['payout_address'],
        'total_supply': data['collection']['stats']['total_supply'],
        'contract_created_date': data['collection']['primary_asset_contracts'][0]['created_date']
        }

    return details


for collection in collections:
    print(f'Working on {collection}')
    data = getCollectionStats(collection)
    collection_report.append(parseCollectionDetails(data))

collections_df = pd.DataFrame(collection_report)
collections_df.to_csv('collections.csv')