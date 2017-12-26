import urllib
import re
from bs4 import BeautifulSoup
import requests
#url = 'https://fossbytes.com/'
url = 'https://fossbytes.com/youtube-on-fire-tv-stick-firefox-workaround/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.status_code) 
#print response.content
soup = BeautifulSoup(response.content,"html.parser")
content =  soup.find_all('div',class_="td-post-content td-pb-padding-side")
#print soup.select('div > p')
 allContent = (elem for elem in content[0].children if getattr(elem, 'name', None) == 'div')
for con in content:
	print con.text.encode('ascii','ignore')
	print con.next_sibling
