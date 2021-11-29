## Background
My foray into the world of Crypto, Blockchain, Web3 would not be complete without a deep dive into the rabbit hole of NFTs.  
As someone who grew up collecting all sorts of trading cards and sports memorabilia, the world of NFTs is both exciting and fascinating.  
This project is dedicated to doing deeper analysis around the concept of "rarity" within the buzzing PFP NFT collection community.  

## Problem Statement
There are many ways to look at rarity, but it is commonly looked at in terms of volumes/frequencies of attributes and traits within a collection.
I feel this can be dissected even further, which gives NFT collectors more information to generate excitement and appreciation for their pieces.

## Solution Intent
This project aims to generate 4 metrics within an NFT collection:  Uniqueness, Rarity, Desirability, and Recognizability.
*Uniqueness* will aggregate which tokens have the least common traits determined statisically by volume and frequency
*Rarity* will measure how significant attributes are comparatively
*Desirability* will measure how much others are interested in NFTs based on their attributes and traits using sales data from NFT marketplaces (namely OpenSea)
*Recognizability* will measure how much of an impression certain NFTs garner based on their digital presence.  (i.e. an NFT owned by a celebrity is more recognizable than one that is not)


## Technical Components
- Mechanism for pulling collection details from Opensea
- Mechanism for pulling Ethereum smart contract details for a collection (typically OpenZeppelin)
- Mechanism for pulling token supply and metadata for each NFT within a collection
- Aggregator that calculates attribute and trait statistics for each collection
-

## Future Work
This project is still in progress.  Some future work that is planned is:
- Component to pull transfer/sales data for NFTs from marketplaces
- Social Media scraping (namely Twitter) for recognizability metrics
- Performance improvements
- Exploration of non-Ethereum chains (Cardano, Solana, Palm, Hive, etc.)
