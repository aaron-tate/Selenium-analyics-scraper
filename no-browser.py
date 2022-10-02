import requests
from bs4 import BeautifulSoup

TRENDING_URL = 'https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all'

#does not execute javascript
response = requests.get(TRENDING_URL)

print('Status Code', response.status_code)

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title:', doc.title)

#find all trends list divs
trends_divs = doc.find_all('div', class_='feed-item-header')

print(f'Found {len(trends_divs)} results')