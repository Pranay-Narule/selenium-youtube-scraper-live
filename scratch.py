import requests
from bs4 import BeautifulSoup


youtubeTrendingVideo = 'https://www.amazon.de/s?me=A1J99ZSJJL0INS'

response = requests.get(youtubeTrendingVideo)
print('Status code', response.status_code)

with open('website.html', 'w') as f:
  f.write(response.text)


doc = BeautifulSoup(response.text, 'html.parser')
print('Page title', doc.title)

# find all video div
Video_divs = doc.find_all('div', class_='style-scope ytd-video-renderer')

# f in front of a string we can use directly variable in {}
print(f'Found {len(Video_divs)} videos')