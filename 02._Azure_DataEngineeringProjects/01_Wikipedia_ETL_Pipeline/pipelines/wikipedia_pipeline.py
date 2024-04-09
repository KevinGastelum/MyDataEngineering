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
  table = soup.find_all('table', {'class': 'wikitable sortable'})[0]

  table_rows = table.find_all('tr')

  return table_rows

def extract_wikipedia_data(**kwargs):
  url = kwargs['url']
  html = get_wikipedia_page(url)
  rows = get_wikipedia_data(html)

  print(rows)