## Webscraping NHL Dataset

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.scrapethissite.com/pages/forms/"

def scrape_page(page_num):
    url = f"{base_url}?page={page_num}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}")
        return [], []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table')  # Adjust this line if the table structure is different
    
    if table is None:
        print(f"Table not found on page {page_num}")
        return [], []  # Return empty lists if no table is found
    
    rows = table.find_all('tr')
  
    headers = [th.get_text() for th in rows[0].find_all('th')]

    data = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        if cols:
            data.append([col.get_text() for col in cols])
    
    return headers, data

all_data = []
page_num = 1

while True:
    headers, data = scrape_page(page_num)
    if not data:  # Stop if no data is returned from the page
        break
    all_data.extend(data)
    page_num += 1

if all_data:
    # Adjust the column names based on your dataset
    column_names = ['Year', 'Win', 'Losses', 'Win %', 'Goals For', 'Goals Against', '+/-']
    df = pd.DataFrame(all_data, columns=column_names)
    df.to_csv("nhl_team_stats.csv", index=False)
else:
    print("No data was scraped.")

df = pd.read_csv("nhl_team_stats.csv")

df['Year'] = df['Year'].astype(int)

wins_1990 = df[df['Year'] == 1990].sort_values('Win', ascending=False).iloc[0]
wins_2000 = df[df['Year'] == 2000].sort_values('Win', ascending=False).iloc[0]
wins_2010 = df[df['Year'] == 2010].sort_values('Win', ascending=False).iloc[0]

print(f"Most wins in 1990: {wins_1990['Team']} with {wins_1990['Win']} wins")
print(f"Most wins in 2000: {wins_2000['Team']} with {wins_2000['Win']} wins")
print(f"Most wins in 2010: {wins_2010['Team']} with {wins_2010['Win']} wins")

teams_1991 = len(df[df['Year'] == 1991])
teams_2001 = len(df[df['Year'] == 2001])
teams_2011 = len(df[df['Year'] == 2011])

print(f"Teams participated in 1991: {teams_1991}")
print(f"Teams participated in 2001: {teams_2001}")
print(f"Teams participated in 2011: {teams_2011}")
