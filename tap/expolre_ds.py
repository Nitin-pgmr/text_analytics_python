import pandas as pd
import logging
import matplotlib
import matplotlib.pyplot as plt
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

file = "../data/un-general-debates/un-general-debates-blueprint.csv"
df = pd.read_csv(file)
logging.debug(df.sample(2))
df['length'] = df['text'].str.len()

logging.debug(df.describe().T)
logging.debug(df[['country', 'speaker']].describe(include='O').T)

# nulls in speakers
logging.debug(df.isna().sum())
df['speaker'].fillna('unknown', inplace=True)
logging.debug(df[df['speaker'].str.contains('Bush')]['speaker'].value_counts())
