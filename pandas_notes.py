# Bring in the pandas library, and shorten it's name to pd
# This is an alias
import pandas as pd

# A series is a one dimensional structure - like a list, or a column. 
# We make two Series objects here
languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
ranking = pd.Series([3,1,2,4])

print(languages)
print(ranking)

# A dataframe is a two dimensional structure - like a dictionary or a table
# Here, we make a dataframe from a list of tuples.
# The dataframe has three rows (one row = one of the tuples) and two columns (as each tuple contains two items)
df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie",55)], columns=["Name", "Age"])
print(df)

# We can make dataframes from existing structures. 
# Here, we use a dictionary to combine our languages and ranking serieses into one table. 
# The keys of the dictionary are the column names, the columns are filled with the series information
df = pd.DataFrame({
    "Languages": languages,
    "Ranking": ranking
})
print(df)

# We can also use pd.concat() to join series together
# Here, we are joining languages and ranking together. axis = 1 means "work along columns"
# In this instance, it will add the two serieses next to eachother, as opposed to on top of each other
df = pd.concat([languages, ranking], axis=1)
# the dataframe object has properties - one of those properties is the fact it has columns
# Here, we access that coloumn property with .notation, and assign a new value.
# This creates our column headers for us!
df.columns = ["Languages", "Ranking"]
print(df)

#W We can bring external files into Pandas to work with. This is very useful, and probably more common than writing data from scratch! 
df = pd.read_csv("speeds.csv")
print(df)

df = pd.read_excel("speeds.xlsx")
print(df)