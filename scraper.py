#import web driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# to eleminate worning
from selenium.webdriver.common.by import By


amazonProductList = 'https://www.amazon.de/s?me=A1J99ZSJJL0INS'

# create function which return the driver
def getDriver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  # don't open UI for chrome
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  # pass options
  driver = webdriver.Chrome(options=chrome_options)
  return driver

# get videos
def getProducts(driver):
  # vedioDivClass = 'style-scope ytd-video-renderer'
  # videoDivs = driver.find_elements_by_class_name(
  #   vedioDivClass
  # )
  vedioDivCLass = 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'
  driver.get(amazonProductList)
  products = driver.find_elements(By.CLASS_NAME,
    vedioDivCLass
  )
  return products

def parseProduct(product):
  print(product)
  productTag = product.find_element(By.TAG_NAME, 'span')
  productTitle = productTag.text
  # url = videoTag.get_attribute('href')
  print('Title', productTitle)
  # print('URL', url)
  return {
    'title': productTitle,
    # 'url': url
  }

if __name__ == "__main__":
  print('Creating driver')
  driver = getDriver()

  print('fetching amazon Products List')
  products = getProducts(driver)
  print(f'Found {len(products)} products', driver.title)
  print('Parsing Products')
  # Get Product title ,Link to the product, Price, Link to the main product image, All bullet points describing the product, Product rating (how many stars product has)
  vedioData = [parseProduct(product) for product in products]
  print(vedioData)

  