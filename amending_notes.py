import pandas as pd

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
ranking = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": ranking
})

# df.loc[4] = ["PHP", 11]
# df.loc[3.5] = ["KESL", 20]
# print(df)

# df = df.sort_index()
# df = df.reset_index(drop=True)
print(df)

new_data = pd.DataFrame({
    "Languages": ["PHP", "TypeScript", "Java"],
    "Ranking": [11, 5, 7]
})

df = pd.concat([df,new_data], ignore_index=True)
print(df)

#--------adding new columns : column reference---------------------
# df["Ranking 2022"] = [4,1,2,3,10,6,5]

# print(df)

#----------adding new columns: concatenation------------------------
new_data_column = pd.DataFrame({
    "Ranking 2022": [4,1,2,3,10,6,5],
    "Ranking 2020": [4,1,2,3,8,5,9],
    "Ranking 2019": [4,1,2,3,8,5,10]
})

df = pd.concat([df,new_data_column], axis=1)

print(df)

# df["Ranking 2020"] = [4,1,2,3,8,5,9]
# df["Ranking 2019"] = [4,1,2,3,8,5,10]

# df.insert(3, "Ranking 2021", [3,1,2,4,11,5,7])
# print(df)

# df.rename(columns={"Ranking" : "Ranking 2023"}, inplace=True)

# df = df.set_index("Languages")
# print(df)

