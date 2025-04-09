import pandas as pd

path = '/Users/qsmy/Documents/models/lawzhidao_filter.csv'

pd_all = pd.read_csv(path)

print(pd_all.sample(n=20))