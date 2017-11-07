import time
import datetime

listoffiles = []
starttime = raw_input("Start time (HH:MM:SS):")
endtime = raw_input("End time (HH:MM:SS): ")


while True :
	newfile = raw_input("Would you like to add file to your list of files(Y/N) :" )
	if newfile == "Y":
		nameoffile = raw_input("Enter name of file : ")
		if nameoffile not in listoffiles:
			listoffiles.append(nameoffile)
			print "Updated listoffiles :",listoffiles
		else:
			print "Error : File already exists in the listoffiles"
			print "Couldn't update listoffiles" ,listoffiles
		
	elif newfile == "N":
		break

countvimeocom = 0
countplayervimeocom = 0
countapivimeocom = 0
linecount = 0
for i in listoffiles:
	with open(i,"r") as f:
		file = f.readlines()
		for line in file:
			linecount += 1
			k =  line.split("|")
			epoch = float(k[0])
			l = time.strftime("%H:%M:%S",time.gmtime(epoch))
			if 500 <= int(k[4]) <= 599 and k[2] == ' player.vimeo.com ' and starttime<= l < endtime :
				countplayervimeocom += 1
			elif 500 <= int(k[4]) <= 599 and k[2] == ' vimeo.com '  and starttime<= l < endtime :
				countvimeocom +=1
			elif 500 <= int(k[4]) <= 599 and k[2] == ' api.vimeo.com ' and starttime<= l < endtime :
				countapivimeocom += 1

	error1 =  format(countplayervimeocom*100/float(linecount), '.2f')
	error2 =  format(countvimeocom*100/float(linecount), '.2f')
	error3 =  format(countapivimeocom*100/float(linecount), '.2f')	

print "Between",starttime,"GMT and",endtime,"GMT:"
print "vimeo.com returned",error2,"% 5xx errors"
print "player.vimeo.com returned",error1,"% 5xx errors"
print "api.vimeo.com returned",error3,"% 5xx errors"


