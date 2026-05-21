import pandas as pd

df = pd.read_csv('movies.csv', skiprows=2)

# Getting to know our data
print(df)
print(df.head()) # first 5
print(df.tail()) # last 5
print(df.describe())
print(df.info())
print(df.sample(5))

df["number_of_years_released"] = 2026 - df["Year"]
print(df.info())
print(df.describe())

mask = df["Year"] > 2020
print(mask)
print(df[df["Year"] > 2020])  # filter data

movies_since_2020_df = df[df["Year"] > 2020]
movies_since_2020_df = movies_since_2020_df[movies_since_2020_df["Genre"].str.lower() == "Sci-Fi".lower()]
movies_since_2020_df[["Title", "Year"]].to_csv('movies_since_2020.csv', index=False)