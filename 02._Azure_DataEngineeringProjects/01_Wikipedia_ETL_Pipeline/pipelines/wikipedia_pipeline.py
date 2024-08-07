import json
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
  text = text.replace('&nbsp', '')
  if text.find(' ♦'):
    text = text.split(' ♦')[0]
  if text.find('[') != -1:
    text = text.split('[')[0]
  if text.find(' (formerly)') != -1:
    text = text.split(' (formerly)')[0]
  if text == '\n':
    return ""
  
  return text.replace('\n', '')

def extract_wikipedia_data(**kwargs):
  url = kwargs['url']
  html = get_wikipedia_page(url)
  rows = get_wikipedia_data(html)

  data = []

  for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    values = {
      'rank': i,
      'stadium': clean_text(tds[0].text),
      'capacity': clean_text(tds[1].text).replace(',', ''),
      'region': clean_text(tds[2].text),
      'country': clean_text(tds[3].text),
      'city': clean_text(tds[4].text),
      'images': 'https://' + tds[5].find('img').get('src').split("//")[1] if tds[5].find('img') else "NO_IMAGE",
      'home_team': clean_text(tds[6].text),
    }
    data.append(values)

  # print(data)
  # data_df = pd.DataFrame(data)
  # data_df.to_csv("data/output.csv", index=False)
  json_rows = json.dumps(data)
  kwargs['ti'].xcom_push(key='rows', value=json_rows)
  return "OK"

def transform_wikipedia_data(**kwargs):
  data = kwargs['ti'].xcom_pull(key='rows', task_ids='extract_data_from_wikipedia')

######## DEBUGGING ########
# print(get_wikipedia_page())
# url = 'https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity'

# html = get_wikipedia_page(url)

# rows = get_wikipedia_data(html)

# for row in rows:
#   print(row)