from bs4 import BeautifulSoup
import requests
import pandas as pd


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
  tables = soup.find_all('table', class_='wikitable')

  # print(f"Found {len(tables)} tables")

  if len(tables) >= 2:
    table_rows = tables[1].find_all('tr') # Table with our data is in index pos 1
    return table_rows
  return []


def clean_text(text):
  text = str(text).strip()

  text = text.replace()

def extract_wikipedia_data(**kwargs):
  url = kwargs['url']
  html = get_wikipedia_page(url)
  rows = get_wikipedia_data(html)

  data = []

  for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    values = {
      'rank': i,
      'stadium': tds[0].text,
      'capacity': tds[1].text,
      'region': tds[2].text,
      'country': tds[3].text,
      'city': tds[4].text,
      'images': tds[5].find('img').get('src').split("//")[1] if tds[5].find('img') else "NO_IMAGE",
      'home_team': tds[6].text,
    }
    data.append(values)
  print(data)
  data_df = pd.DataFrame(data)
  data_df.to_csv("data/output.csv", index=False)
  return data

######## DEBUGGING ########
# print(get_wikipedia_page())
# url = 'https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity'

# html = get_wikipedia_page(url)

# rows = get_wikipedia_data(html)

# for row in rows:
#   print(row)








