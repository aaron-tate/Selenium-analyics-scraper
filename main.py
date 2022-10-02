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

if __name__ == "__main__":
  print('Creating Driver')
  driver = get_driver()

  print('Fetching the Page')
  driver.get(TRENDING_URL)
  print('Page title:', driver.title)

  print('scraping page for specific divs')
  T_ITEMS_DIV_TAG = 'md-list'
  items_divs = driver.find_elements(By.TAG_NAME, T_ITEMS_DIV_TAG)

  print(f'Found {len(items_divs)} items')
  
  
  
