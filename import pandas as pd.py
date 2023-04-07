import pandas as pd

df0 = pd.DataFrame()
print(df0.head())




data = {'Prénom': ['Amine', 'Sarra', 'Malek', 'Ahmed'],
        'Age': [14, 15, 15, 13],
        'Ville': ['Sousse', 'Gafsa', 'Bizerte', 'Gabes']}

df1 = pd.DataFrame(data)
print(df1)







fifa2018 = pd.read_excel(r"C:/Users/firas/Desktop/fifa2018.xlsx", sheet_name="Teams")
print(fifa2018)




stock = pd.read_csv(r"C:/Users/firas/Desktop/stock.csv", sep=";")
#print(stock.head())

print(stock)

print(f"Dimensions: {stock.shape}")

print(f"Number of elements: {stock.size}")

print(stock.info())

print(stock.describe())

print(stock.columns)



stock1 = stock.rename(columns={"QT": "Quantite"})

stock2 = stock.drop("QT", axis=1)

stock3 = stock.drop([0] + list(range(4, 30, 5)) + list(range(3)))

print(stock["Article"])

print(stock[["Article", "QT"]])

print(stock.loc[10:19, "Article"])

print(stock.iloc[6])

print(stock.head(20))


print(stock.tail(10))

print(stock.iloc[25:30])

print(stock.iloc[17, 1])

stock.loc[0, "QT"] = 30

stock.iloc[19] = ["Houe", 29.525, 400]

stock["PrixTotalHT"] = 0

stock["PrixTotalHT"] = stock["PU"] * stock["QT"]

stock["TVA"] = 0.19 * stock["PrixTotalHT"]

stock["PrixTotalTTC"] = stock["PrixTotalHT"] + stock["TVA"]

#13
stock4 = stock.drop_duplicates()

#14
stock5 = stock4.dropna()

#15
stock6 = stock4.dropna(axis=1)


#16
print("Average quantity:", stock["Quantite"].mean())


#17
print("Minimum price:", stock["PU"].min())
print("Maximum price:", stock["PU"].max())


#18
total_ttc = (stock["Quantite"] * stock["PrixTotalTTC"]).iloc[:5].sum()
print("Total TTC for the first 5 articles:", total_ttc)

#19
total_ttc = (stock["Quantite"] * stock["PrixTotalTTC"]).sum()
print("Total TTC for all articles:", total_ttc)






