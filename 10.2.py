import pandas as pd

data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "Goa", "Punjab"],
    "Area": [307713, 196024, 342239, 3702, 50362],
    "Population": [112374333, 60439692, 68548437, 1458545, 27743338]
}

df = pd.DataFrame(data)

print("\nState Details:")
print(df)

print("\nState with Largest Area:")
print(df[df['Area'] == df['Area'].max()]['State'])

print("\nState with Largest Population:")
print(df[df['Population'] == df['Population'].max()]['State'])

df['Density'] = df['Population'] / df['Area']
print("\nPopulation Density:")
print(df[['State', 'Density']])

print("\nState with Highest Population Density:")
print(df[df['Density'] == df['Density'].max()]['State'])