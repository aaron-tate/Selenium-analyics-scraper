import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

TRENDING_URL = 'https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all'


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def get_items(driver):
  driver.get(TRENDING_URL)
  T_ITEMS_DIV_TAG = 'feed-item'
  items = driver.find_elements(By.TAG_NAME, T_ITEMS_DIV_TAG)
  return items

def parse_item(item):
  title_CLASS = item.find_element(By.TAG_NAME, 'a')
  title = title_CLASS.text

  imageurl_class = item.find_element(By.CLASS_NAME, 'feed-item-image-wrapper')
  imageurl = imageurl_class.find_element(By.TAG_NAME, 'img').get_attribute('ng-src')
  
  source_tag = item.find_element(By.CLASS_NAME, 'source-and-time')
  source = source_tag.text

  description_tag = item.find_element(By.CLASS_NAME, 'summary-text')
  description = description_tag.text

  url_tag = item.find_element(By.LINK_TEXT, description)
  url = url_tag.get_attribute('href')
  
  
  return{
    'Title:': title,
    'source': source,
    'Short Description': description,
    'url': url,
    'imageurl': imageurl
  }

if __name__ == "__main__":
  print('Creating Driver')
  driver = get_driver()

  print('Fetching the Trending topics')
  items = get_items(driver)

  print(f'Found {len(items)} items')

  print('parsing the top topics')
  items_data = [parse_item(item) for item in items[:12]]

  print(items_data)

  print('Saving data to a .csv')
  topics_df = pd.DataFrame(items_data)
  print(topics_df)
  topics_df.to_csv('trendingtopics.csv', index=None)
