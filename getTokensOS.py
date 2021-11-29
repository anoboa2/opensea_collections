import requests
import pandas as pd


collections = [
    'cryptopunks',
    'boredapeyachtclub',
    'mutant-ape-yacht-club',
    'cryptoadz-by-gremplin',
    'neo-tokyo-identities',
    'doodles-official',
    'cool-cats-nft',
    'cyberkongz',
    'the-doge-pound',
    'meebits',
    # 'veefriends',
    'mekaverse',
    'creature-world-collection',
    'lazy-lions',
    'pudgypenguins',
    'deadfellaz',
    'sneaky-vampire-syndicate',
    'bored-ape-kennel-club',
    'world-of-women-nft',
    'supducks',
    # 'bears-deluxe',
    'the-sevens-official',
    'thehumanoids',
    'thecryptodads',
    'robotos-official'
    ]

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

def parseTraits(data):
    attributes = list(data['collection']['traits'].keys())
    trait_counts = data['collection']['traits']
    
    return attributes, trait_counts



for collection in collections:
    print(f'Working on {collection}')
    data = getCollectionStats(collection)
    attributes, traits = parseTraits(data)
    d = []

    for attribute in attributes:
        for trait, count in traits[attribute].items():
            results = {
                'Attribute': attribute,
                'Trait': trait,
                'Count': count,
            }
            d.append(results)
    
    distribution = pd.DataFrame(d)

    for index, row in distribution.iterrows():
        distribution.loc[index, 'Trait_Frequency'] = row['Count'] / sum(distribution[distribution['Attribute']==row['Attribute']]['Count'])
        distribution.loc[index, 'Overall_Frequency'] = row['Count'] / parseCollectionDetails(data)['total_supply']
        distribution.loc[index, 'Attribute_Frequency'] = len(distribution[distribution['Attribute']==row['Attribute']]) / len(distribution['Attribute'])

    for attribute in attributes:
        trait_rank = {}
        subset = distribution[distribution['Attribute'] == attribute]['Trait_Frequency'].drop_duplicates()
        rank = subset.sort_values().reset_index()
        for index, row in rank.iterrows():
            trait_rank[row['Trait_Frequency']] = index+1
        for index, row in distribution[distribution['Attribute']==attribute].iterrows():
            distribution.loc[index, 'Trait_Rank'] = trait_rank[row['Trait_Frequency']]

    distribution['Overall_Rank'] = list(map(lambda x: x+1, distribution['Overall_Frequency'].sort_values().reset_index().sort_values('index').index))
    distribution = distribution.assign(Symbol=parseCollectionDetails(data)['symbol'])

    for index, row in distribution.iterrows():
        distribution.loc[index, 'Rarity_Score'] = row['Trait_Frequency'] * row['Overall_Frequency'] * row['Attribute_Frequency']

    distribution = distribution[['Symbol', 'Attribute', 'Trait', 'Count', 'Trait_Frequency', 'Trait_Rank', 'Overall_Frequency', 'Overall_Rank', 'Attribute_Frequency', 'Rarity_Score']]
    distribution.to_csv(f'distributions/{collection}_distribution.csv')