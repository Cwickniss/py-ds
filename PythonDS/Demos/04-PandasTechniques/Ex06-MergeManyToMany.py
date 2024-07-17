import pandas as pd

df1 = pd.DataFrame({
    'name': ['Andy', 'Jayne', 'Em', 'Tom'],
    'region': ['Wales', 'Wales', 'N England', 'S England']
})

df2 = pd.DataFrame({
    'region': ['Wales', 'S England', 'S England', 'N England', 'N England'],
    'city':   ['Swansea', 'London', 'Bristol', 'Manchester', 'Leeds']
})

# Do a many-to-many merge, based on the common 'region' column. 
df3 = pd.merge(df1, df2)

# Bonus bit: Add a new column that indicates the first occurrence of a region.
df3['first_occurrence_of_region'] = df3.groupby('region').cumcount() == 0
print('\ndf3\n', df3)