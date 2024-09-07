import pandas as pd

data_url = 'https://drive.google.com/uc?export=download&id=1_XrycolWv3gMgT16C8-Koyj77ZXr-T-k'
df = pd.read_csv(data_url)


df.to_csv('../data/malinda_data.csv', index=False)
print("Data collection completed by Malinda")

