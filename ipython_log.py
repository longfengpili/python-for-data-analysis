# IPython log file

get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('logstart', '')
import pandas as pd
import pandas as pd
from pandas import Series,DataFrame
obj = Series(['c','a','d','a','a','b','b','c','c'])
obj
uniques = obj.unique()
uniques = obj.unique()
uniques
obj.value_counts
obj.value_counts()
obj.values()
obj.values
pd.value_counts(obj.values,sort=False)
mask = obj.isin(['b','c'])
mask
obj[mask]
data = DataFrame({'qu1':[1,3,4,3,4],'qu2':[2,3,1,2,3],'qu3':[1,5,2,4,4]})
data
pd.value_counts(data)
get_ipython().run_line_magic('pinfo', 'pd.value_counts')
pd.value_counts(data.values)
pd.value_counts(data.values)
data.values
data.apply(pd.value_counts)
counts = data.apply(pd.value_counts)
counts.plot(kind='bar')
get_ipython().run_line_magic('matplatlib', '')
get_ipython().run_line_magic('matplatlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'inline')
counts.plot(kind='bar')
string_data = Series(['aardvark','artichoke','np.nan','avocado'])
string_data
string_data = Series(['aardvark','artichoke',np.nan,'avocado'])
import numpy as np
string_data = Series(['aardvark','artichoke',np.nan,'avocado'])
string_data
string_data.isnull()
string_data.isna()
string_data.isnull()
string_data.isna()
from numpy import nan as NA
data = Series([1,NA,3.5,NA,7])
data
data.dropna()
data.drop()
data.drop
data.notnull()
data = DataFrame([1,6.5,3],[1,NA,NA],[NA,NA,NA],[NA,6.5,3])
data = DataFrame([[1,6.5,3],[1,NA,NA],[NA,NA,NA],[NA,6.5,3]])
data
data.dropna()
data.dropna(how='all')
data[4]=NA
data
data.dropna(axis=1,how='all')
df = DataFrame(np.random.randn(7,3))
df
df.ix[:2,1] = NA
df
df.loc[:3,2] = NA
df
df.dropna()
df.dropna(thresh=1)
df.dropna(thresh=2)
df.dropna(thresh=4)
df.dropna(thresh=0)
df.dropna(thresh=1)
df.dropna(thresh=2)
df.dropna(thresh=3)
df.dropna(thresh=4)
df.dropna(thresh=3)
get_ipython().run_line_magic('logstart', '')
df.dropna(thresh=1)
df.dropna(thresh=2)
df.fillna(0)
df
df.fillna({1:0.5,2:1,4:4})
_
__
print(_)
get_ipython().system('pwd')
get_ipython().system('cd')
_
_ = df.fillna(0,inplace=True)
df
df = DataFrame(np.random.randn(6,3))
df.loc[2:,1] = NA;df.loc[4:,2] = NA
df
df.fillna(mmethod='ffill')
df.fillna(method='ffill')
data = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])
data
data.index
data['b']
data['b']['1']
data['b'][:1]
data[:,2]
data['b'][1]
df
df[0]
df[:0]
frame = DataFrame(np.arange(12).reshape(4,3))
frame
frame = DataFrame(np.arange(12).reshape(4,3),index=[['a','a','b','b'],[1,2,1,2]],columns=[['ohio','ohio','colorado'],['green','red','green']])
frame
frame['a']
frame[a]
frame['a']
frame['ohio']
frame['ohio']['a']
frame['ohio']['a':]
frame['ohio'][['a',]]
frame['ohio'][['a']]
frame['ohio']['a']
frame['ohio'][:'a']
frame['ohio'][:'a'][1]
frame['ohio'][:'a'][:1]
frame[:'a'][:1]
frame[:'a']
import pandas as pd
from pandas import Series,DataFrame
obj = Series(['c','a','d','a','a','b','b','c','c'])
obj
uniques = obj.unique()
uniques
obj.value_counts()
