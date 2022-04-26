#import web driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# to eleminate worning
from selenium.webdriver.common.by import By


youtubeTrendingVideo = 'https://m.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

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
def getVideos(driver):
  # vedioDivClass = 'style-scope ytd-video-renderer'
  # videoDivs = driver.find_elements_by_class_name(
  #   vedioDivClass
  # )
  vedioDivTag = 'ytd-video-renderer'
  driver.get(youtubeTrendingVideo)
  videos = driver.find_elements(By.TAG_NAME,
    vedioDivTag
  )
  return videos

def parseVideo(video):
  videoTag = video.find_element(By.ID, 'video-title')
  videoTitle = videoTag.text
  url = videoTag.get_attribute('href')
  print('Title', videoTitle)
  print('URL', url)
  return {
    'title': videoTitle,
    'url': url
  }

if __name__ == "__main__":
  print('Creating driver')
  driver = getDriver()

  print('fetching trending videos')
  videos = getVideos(driver)
  print(f'Found {len(videos)} videos', driver.title)
  print('Parsing top 2 videos')
  # title,url, thumbnail_url, channel, views, upload,     description
  vedioData = [parseVideo(video) for video in videos[:2]]
  print(vedioData)

  