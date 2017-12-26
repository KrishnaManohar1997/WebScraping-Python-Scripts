import urllib
import re
from bs4 import BeautifulSoup
reg = 401
while reg<560:
	Details=[]
	Marks = []
	url= 'http://becbapatla.ac.in/STUDENTINFO/StuInfofinal.jsp?id=y14ace'+str(reg)
	#url= 'http://becbapatla.ac.in/STUDENTINFO/StuInfofinal.jsp?id=y14acs463'
	raw= urllib.urlopen(url)
	code = raw.read()
	soup = BeautifulSoup(code,'html.parser')
	det= soup.find_all('td',align='Left')
	fdetails = soup.find_all('td',align='left')
	sems = soup.find_all('font',size='3em')
	marks = soup.find_all('td',align='center')
	noRecord = soup.find_all('font',color='Red')
	finalText = soup.find_all('font',size='4em')
	#print noRecord[0].text
	if(len(noRecord)!=1):
		#marks = soup.find_all('tr')
		#print len(sems)
		d = ('Student Details  ==->   %s\t%s\t%s'%(det[0].text,det[1].text,fdetails[0].text))
		Details.append(d)
		print Details[0]
		print "Code \t Title \t\t Externals \t\t Internals \t\t Total \t\t GPA \t\t Credits"
		for m in marks:
			Marks.append((re.sub(r'[^\x00-\x7F]+','',m.text)).strip())
		# for j in Marks:
			# print j
		m=0
		lop=1
		count = 0
		print len(Marks)
		print "Semester "+str(lop)
		#while lop < len(sems):
		while m < len(Marks):
			if(count!=9):
				print ('%s\t \t%s\t \t%s\t \t%s\t \t%s\t \t%s'%(Marks[m],Marks[m+1],Marks[m+2],Marks[m+3],Marks[m+4],Marks[m+5]))
				m+=7
				count+=1
			else:
				#print ('\nTotal %s\t\t%s\t\t%s\t\t%s\t\t%s'%(Marks[m],Marks[m+1],Marks[m+2],Marks[m+3],Marks[m+4]))
				print "\nTotal External "+Marks[m]
				print "Total Internal  "+Marks[m+1]
				print  "Total Marks  "+Marks[m+2][:3]
				#print "SGPA        "+Marks[m+3]
				print "Total Credits "+Marks[m+4]+"\n\n"
				m+=6
				count=0
				lop=lop+1
				if(lop<=len(sems)):
					print "\t\t\t\t\t Semester "+str(lop)+"\n"
			#		print "Semester "+str(lop+1)
			#lop=lop+1
		print finalText[0].text
		print '------------------------------------------------------------------------------'
		reg=reg+1
	else:
		print "Record Not Found\n------------------------------------------------------------------------------------"
		reg=reg+1
		continue
	