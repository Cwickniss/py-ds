import pandas as pd

stats = [ 
    {'name': 'Andy',  'born': 1964, 'height': 167, 'weight': 60.0},
    {'name': 'Jayne', 'born': 1965, 'height': 170, 'weight': 65.0}, 
    {'name': 'Em',    'born': 1997, 'height': 165, 'weight': 58.0}, 
    {'name': 'Tom',   'born': 1997, 'height': 177, 'weight': 70.0}
]

# Create a DataFrame with specified data and implicit column names. 
df = pd.DataFrame(stats)
print(df)