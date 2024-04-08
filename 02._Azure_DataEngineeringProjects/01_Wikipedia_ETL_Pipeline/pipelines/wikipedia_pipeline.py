from bs4 import BeautifulSoup


def get_wikipedia_page(url):
  import requests

  print("Getting wikipedia page...", url)

  try:
    response = requests.get(url, timeout=10)
    response.raise_for_status() # Checks if requests was succesful

    return response.text
  except requests.RequestException as e:
    print(f'An error ocurred: {e}')

def get_wikipedia_data(html):
  soup = BeautifulSoup(html, 'htnl.parser')
  table = soup.find_all('table', {'class': 'wikitable sortable'})[0]

  table_rows = table.find_all('tr')

  return table