# import for CSV
import pandas as pd
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
  # driver.implicitly_wait(10)
  return driver

# get videos
def getProducts(driver, i):
  # vedioDivClass = 'style-scope ytd-video-renderer'
  # videoDivs = driver.find_elements_by_class_name(
  #   vedioDivClass
  # )
  driver.get(amazonProductList)
  # i =1
  # products = driver.find_elements(By.XPATH,f"//div[@data-index='1']")
  # while (driver.find_elements(By.XPATH,f"//div[@data-index='{i}']")):
  #   print(f"//div[@data-index='{i}']")
  #   vedioDivCLass = f'MAIN-SEARCH_RESULTS-{i}'
  #   products = driver.find_elements(By.ID,
  #     vedioDivCLass
  #   )
  #   products = driver.find_elements(By.XPATH,f"//div[@data-index='{i}']")
  #   i+=1
  products = driver.find_elements(By.XPATH,f"//div[@data-index='{1}']")
  return products

def parseProduct(product):
  # print(product)
  productTag = product.find_element(By.CLASS_NAME, 'a-text-normal')
  productPriceClass = product.find_element(By.CLASS_NAME, 'a-price')
  imageLinkClass = product.find_element(By.CLASS_NAME, 's-no-outline')
  ratingClass = product.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/span[1]/span/a/i[1]/span')
  productPrice = productPriceClass.text
  productTitle = productTag.text
  rating = ratingClass.get_attribute("innerHTML")
  url = productTag.get_attribute('href')
  imageUrl = imageLinkClass.get_attribute('href')
  print('Title', productTitle)
  print('URL', url)
  return {
    'title': productTitle,
    'url': url,
    'price': productPrice,
    'imageUrl': imageUrl,
    'rating': rating
  }

def repeat():
  i=1
  products = driver.find_elements(By.XPATH,f"//div[@data-index='1']")
  while (driver.find_elements(By.XPATH,f"//div[@data-index='{i}']")):
    # print(f"//div[@data-index='{i}']")
    # vedioDivCLass = f'MAIN-SEARCH_RESULTS-{i}'
    # products = driver.find_elements(By.ID,
    #   vedioDivCLass
    # )
    # products = driver.find_elements(By.XPATH,f"//div[@data-index='{i}']")
    # i+=1

if __name__ == "__main__":
  print('Creating driver')
  driver = getDriver()

  print('fetching amazon Products List')
  products = getProducts(driver,1)
  print(f'Found {len(products)} products', driver.title)
  print('Parsing Products')
  # Get Product title ,Link to the product, Price, Link to the main product image, All bullet points describing the product, Product rating (how many stars product has)
  productData = [parseProduct(product) for product in products]
  print(productData)
  print('save to CSV file')
  # create a data frame
  productsDf = pd.DataFrame(productData)
  print(productsDf)
  # save to CSV
  productsDf.to_csv('products.csv', index=None)

  