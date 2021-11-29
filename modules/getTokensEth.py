import requests
import json
import pandas as pd
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://cloudflare-eth.com"))

def callHTTP(tokenURI):
    response = requests.get(tokenURI).json()

    return response


def callIPFS(tokenURI):
    endpoint = "http://127.0.0.1:5001/api/v0/object/data?arg="
    cid_path = tokenURI[7:]

    response = json.loads(requests.post(endpoint+cid_path).text[5:-3])

    return response


def getTokens(contract_address, slug, total_supply):
    print(f'Getting contract info for {slug}')

    tokenABI = [
        {
            "inputs": [{"internalType": "uint256", "name": "tokenID", "type": "uint256"}],
            "name": "tokenURI",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view", "type": "function"
        }
    ]

    contract = w3.eth.contract(address=w3.toChecksumAddress(contract_address), abi=tokenABI)

    attributes = list(pd.read_csv(f'distributions/{slug}_distribution.csv')['Attribute'].value_counts().index)
    headers = ["name", "tokenId", "image"] + attributes

    data = []

    for i in range(int(total_supply)):
        try:
            tokenURI = contract.functions.tokenURI(w3.toInt(i)).call()
            # print(f'Located tokenURI for token #{i}')
        except ValueError:
            print(f'{slug} does not have a token #{i}')
            continue
        
        if "http" in tokenURI:
            # print(f'tokenURI uses an HTTP path')
            metadata = callHTTP(tokenURI)
        elif "ipfs://" in tokenURI:
            # print(f'tokenURI uses an IPFS path')
            metadata = callIPFS(tokenURI)
        else:
            print(f'Metadata cannot be retrieved from tokenURI for token #{i} of {slug}')
            continue

        schema = {}

        try:
            schema['name'] = metadata['name']
        except KeyError:
            schema['name'] = None
            # print('There is no Name value for this token')

        try:
            schema['tokenId'] = metadata['tokenId']
        except KeyError:
            schema['tokenId'] = None
            # print('There is no tokenId value for this token')

        try:
            schema['image'] = metadata['image']
        except KeyError:
            schema['image'] = None
            # print('There is no Image value for this token')


        for attribute in metadata['attributes']:
            # print(f'Parsing attributes for token #{i}')
            schema[attribute['trait_type']] = attribute['value']

        data.append(schema)
        print(f'Token #{i} successfully captured')
    
    return data, headers
