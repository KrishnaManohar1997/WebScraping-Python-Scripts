import urllib
from bs4 import BeautifulSoup
Movies = []
Ratings = []
Years = []
MovieNum=1
for j in range(5):
	url = 'http://www.imdb.com/search/title?groups=top_250&sort=user_rating&page='+str(j+1)+'&ref_=adv_nxt'
	f = urllib.urlopen(url)
	code = f.read()
	########################################################################
	
	
	
	Logic is Hidden for Security purposes
	
	
	
	
	Logic is Hidden for Security purposes
	
	
	
	
	Logic is Hidden for Security purposes
	
	
	
	
	Logic is Hidden for Security purposes
	
	
	
	
	##############################################################################
	
	
	
mov=0
while mov < len(Movies):
	print Movies[mov]+str("\t Rating ")+Ratings[mov]+str("\t Year  ")+Years[mov]
	mov=mov+1
