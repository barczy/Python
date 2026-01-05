############################
## Pandas: data manipulation, series (sorozatok) and dataframe(excel tábla)
############################
##
## Arrays

import yaml
import pandas as pd
data=[1,2,3,4,5]
series = pd.Series(data)
print(series)

data=[1,2,3,4,5]
index=['a','b','c','d','e']
series = pd.Series(data, index=index)
print(series)

## from dictionary of list
data = {
    "name": ['Krish', 'John', 'Jack'],
    "age": [25, 30, 45],
    'city' : ['Florida', 'Berlin', 'London']
}
dataframe = pd.DataFrame(data)
print(dataframe)

## from list of dictionaries
data = [
    {"name": 'Krish', 'age':32, 'city': 'Florida'},
    {"name": 'Jack', 'age':22, 'city': 'Florida'},
    {"name": 'Jill', 'age':42, 'city': 'London'}
]
dataframe = pd.DataFrame(data)
print(dataframe)
print(dataframe.head(2)) #eleje
print(dataframe.tail(2)) #vége
print(dataframe['name']) #oszlop
print(dataframe.loc[1]) #sor
print(dataframe.at[1,'name']) #adott cella
print(dataframe.iat[1,1]) #adott cella
dataframe['salary']=[500,600,700] #add a column
print(dataframe.describe()) #statisztikai adatok
print(dataframe.dtypes) #oszlopok típusai
print(dataframe.isnull()) #van-e hiányzó érték, True, ahol van
print(dataframe.isnull().sum())
dataframe = dataframe.rename(columns={'name':'New name'}) #átnevezés
dataframe["New value"]=dataframe['salary'].apply(lambda x:x*2) #függvény alkalmazása
## .astpye(int) típus módosítás
print(dataframe)

## Group and aggregation
grouped=dataframe.groupby('city')['age'].mean() #csoportosít, átlagot számít
print(grouped)
## Merging and joining Dataframes
## df = pd.read_csv("data.csv")
df1 = pd.DataFrame({'Key':['A','B','C'], 'Value1':[1,2,3]})
df2 = pd.DataFrame({'Key':['A','B','D'], 'Value2':[4,5,6]})
print (df1, df2)
print(pd.merge(df1, df2, on="Key", how="inner"))
print(pd.merge(df1, df2, on="Key", how="outer")) #left outer, right outer, ...

## Read from different sources
## from json: pd.read_json()
## to json pd.to_json()
## from csv: pd.read_csv()
## to csv: pd.to_csv()
## from HTML (!), weblapokról táblzatokból pd.read_html, <table> elemeket keresi
## from excel: pd.read_excel()

# Load YAML file
with open('data.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Convert to DataFrame (if the structure is tabular)
df = pd.DataFrame(yaml_data)

print(df)
