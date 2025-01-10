import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Pokémon database table
url = "https://pokemondb.net/pokedex/all"

# Send a GET request to the webpage
response = requests.get(url)
response.raise_for_status()  # Raise an error for failed requests

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing Pokémon data
table = soup.find('table', {'id': 'pokedex'})

# Extract table headers
headers = [header.text for header in table.find('thead').find_all('th')]

# Extract table rows
rows = []
for row in table.find('tbody').find_all('tr'):
    cells = row.find_all(['td', 'th'])
    row_data = [cell.text.strip() for cell in cells]
    rows.append(row_data)

# Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=headers)

# Normalize column names by stripping extra whitespace
df.columns = [col.strip() for col in df.columns]

# Debug: Print the column names
print("Columns in DataFrame:", df.columns)

# Adjust column names to match extracted data
df.rename(columns={
    'Type': 'Type 1',  # Renaming to match expected structure
}, inplace=True)

# Convert relevant columns to numeric
numeric_columns = ['#', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')

# Check if 'Type 1' exists
if 'Type 1' not in df.columns:
    raise KeyError("'Type 1' column not found. Check the scraped table structure.")

# 1. Find the strongest Pokémon of each type
strongest_by_type = df.groupby('Type 1').apply(lambda x: x.loc[x['Total'].idxmax()])
print("Strongest Pokémon by Type 1:\n", strongest_by_type[['Name', 'Type 1', 'Total']])

# 2. Find the best attackers
best_attackers = df.nlargest(10, 'Attack')[['Name', 'Attack', 'Type 1']]
print("\nBest Attackers:\n", best_attackers)

# 3. Calculate averages of stats for each type
average_stats_by_type = df.groupby('Type 1')[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].mean()
print("\nAverage Stats by Type 1:\n", average_stats_by_type)

# 4. Additional Analysis
# a. Find the fastest Pokémon
fastest_pokemon = df.nlargest(10, 'Speed')[['Name', 'Speed', 'Type 1']]
print("\nFastest Pokémon:\n", fastest_pokemon)

# b. Pokémon with the highest special attack
best_special_attackers = df.nlargest(10, 'Sp. Atk')[['Name', 'Sp. Atk', 'Type 1']]
print("\nBest Special Attackers:\n", best_special_attackers)

# c. Count of Pokémon per primary type
pokemon_count_by_type = df['Type 1'].value_counts()
print("\nCount of Pokémon by Type 1:\n", pokemon_count_by_type)

# Optionally save the DataFrame to a CSV file
df.to_csv("pokemon_data.csv", index=False)



Columns in DataFrame: Index(['#', 'Name', 'Type', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk',
       'Sp. Def', 'Speed'],
      dtype='object')
Strongest Pokémon by Type 1:
                                    Name         Type 1  Total
Type 1                                                       
Bug                              Pinsir            Bug    500
Bug Dark                          Lokix       Bug Dark    450
Bug Electric                   Vikavolt   Bug Electric    500
Bug Fairy                      Ribombee      Bug Fairy    464
Bug Fighting   Heracross Mega Heracross   Bug Fighting    600
...                                 ...            ...    ...
Water Ice                        Lapras      Water Ice    535
Water Poison                 Tentacruel   Water Poison    515
Water Psychic      Slowbro Mega Slowbro  Water Psychic    590
Water Rock                   Carracosta     Water Rock    495
Water Steel                    Empoleon    Water Steel    530

[221 rows x 3 columns]

Best Attackers:
                          Name  Attack            Type 1
201      Mewtwo Mega Mewtwo X     190  Psychic Fighting
274  Heracross Mega Heracross     185      Bug Fighting
956                   Kartana     181       Grass Steel
...
Grass Water         1
Grass Rock          1
Poison Ghost        1
