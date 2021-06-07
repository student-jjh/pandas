import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/Users/junjoonheak/Desktop/pandas_study/doit_pandas-master/data/gapminder.tsv',sep='\t')
'''
print(df.head())

print(df.shape)

country_df=df["country"]

print(country_df.head())

subset=df[["country",'continent',"year"]]

print(subset.head())

print(df.loc[0])
'''
subset1=df.loc[:]
subset2=df.iloc[:,[2,4,-1]]

small_range=list(range(5))
subset3=df.iloc[[0,99,999],0:6:2]
grape_thing=subset1.groupby('continent')['lifeExp'].nunique()

'''plt.plot(grape_thing)
plt.show()
'''
