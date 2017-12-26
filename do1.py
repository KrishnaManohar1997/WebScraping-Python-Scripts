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
	soup = BeautifulSoup(code,"html.parser")
	imgs = soup.find_all("img")
	ratings = soup.find_all("div")
	years = soup.find_all("span", class_="lister-item-year text-muted unbold")
	#print k
	for movieName in imgs:
		if (movieName.attrs['alt']=='IMDbPro Menu' or movieName.attrs['alt'] == 'Go to IMDbPro'):
			continue
		else:
			#print movieName.attrs['alt']
			
			Movies.append(str(MovieNum)+str("  ")+movieName.attrs['alt'])
			MovieNum=MovieNum+1
	for rats in ratings:
		try:
		#if(rats.attrs['name'] =='ir'):
		#Movies.append(str(MovieNum)+str("  ")+movieName.attrs['alt'])
			MovieRating = rats.attrs['data-value']
			Ratings.append(MovieRating)
		except:
			continue
	for year in years:
		if year.text.find('I') == 1:
			Years.append((year.text.lstrip('(I) (')).rstrip(')'))
		else:
			Years.append((year.text.lstrip('(')).rstrip(')'))
mov=0
while mov < len(Movies):
	print Movies[mov]+str("\t Rating ")+Ratings[mov]+str("\t Year  ")+Years[mov]
	mov=mov+1
#k = soup.find_all("span")
# for year in k:
	# try:
		# if(year.attrs['class']=="lister-item-year text-muted unbold"):
			# print year
	# except:
		# continue