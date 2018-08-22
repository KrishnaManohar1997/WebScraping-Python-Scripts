import urllib
import re
from bs4 import BeautifulSoup
reg = 401
while reg<560:
	Details=[]
	Marks = []
	########################################################################
	
	
	
	Logic is Hidden for Security purposes
	
	
	
	
	Logic is Hidden for Security purposes
	
	
	
	
	Logic is Hidden for Security purposes
	
	
	
	
	##############################################################################
		while m < len(Marks):
			if(count!=9):
				print ('%s\t \t%s\t \t%s\t \t%s\t \t%s\t \t%s'%(Marks[m],Marks[m+1],Marks[m+2],Marks[m+3],Marks[m+4],Marks[m+5]))
				m+=7
				count+=1
			else:
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
		print finalText[0].text
		print '------------------------------------------------------------------------------'
		reg=reg+1
	else:
		print "Record Not Found\n------------------------------------------------------------------------------------"
		reg=reg+1
		continue
	
