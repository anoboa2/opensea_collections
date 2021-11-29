import os
import pandas as pd

master_collections = pd.DataFrame(columns=['Symbol', 'Attribute', 'Trait', 'Count', 'Trait_Frequency', 'Trait_Rank', 'Overall_Frequency', 'Overall_Rank', 'Attribute_Frequency', 'Attribute_std_dev', 'Rarity_Score'])

path, dirs, files = next(os.walk("distributions"))

for f in files:
    df = pd.read_csv('distributions/'+f, index_col=0)
    master_collections = master_collections.append(df, ignore_index=True)

master_collections.to_csv('master_distribution.csv')

print(master_collections.value_counts('Symbol'))