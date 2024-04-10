from bs4 import BeautifulSoup
import requests


def get_wikipedia_page(url):
  print("Getting wikipedia page...", url)

  try:
    response = requests.get(url, timeout=10)
    response.raise_for_status() # Checks if requests was succesful

    return response.text
  except requests.RequestException as e:
    print(f'An error ocurred: {e}')

def get_wikipedia_data(html):
  soup = BeautifulSoup(html, 'html.parser')
  tables = soup.find_all('table', class_='wikitable sortable sticky-header jquery-tablesorter')

  if len(tables) >= 2:
    table_rows = tables[0].find_all('tr')
    return table_rows
  return []

#   print(f"Found {len(tables)} tables with class 'wikitable sortable'")

#   for i, table in enumerate(tables):
#       print(f"Table {i}:")
#       print(table)
#       print("\n")

# # Assuming the first table is the one we want
#   if tables:
#       table_rows = tables[0].find_all('tr')
#       return table_rows
#   return []

  # table_rows = table.find_all('tr')

  # return table_rows

def extract_wikipedia_data(**kwargs):
  url = kwargs['url']
  html = get_wikipedia_page(url)
  rows = get_wikipedia_data(html)

  print(rows)

# print(get_wikipedia_page())
url = 'https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity'

html = get_wikipedia_page(url)

rows = get_wikipedia_data(html)

for row in rows:
  print(row)
