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
    T_ITEMS_DIV_TAG = 'md-list'
    items = driver.find_elements(By.TAG_NAME, T_ITEMS_DIV_TAG)
    return items

if __name__ == "__main__":
  print('Creating Driver')
  driver = get_driver()

  print('Fetching the Trending topics')
  items = get_items(driver)
  
  print(f'Found {len(items)} items')

  print('parsing the first topic')
  #info being parsed: rank in top ten, title, news outlet, short description, and thumbnail

  item = items[1]
  title_CLASS= item.find_element(By.TAG_NAME, 'a')
  title = title_CLASS.text

  description_tag = item.find_element(By.CLASS_NAME, 'summary-text')
  description = description_tag.text 

  source_tag = item.find_element(By.CLASS_NAME, 'source-and-time')
  source = source_tag.text
  
  print('Title:', title)
  print('Short Description:', description)
  print('', source)
