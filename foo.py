import os
import sys
import re

file = open(sys.argv[1],'r')

try:
	for line in file:
		#result = re.findall("?<=FP=",line)
		relays = line.split("<div style=\"font-size:1.2em; margin-bottom:10px;\">")
		for relay in relays:
			if relay.find("has set up") > -1:
				names = relay.split("<strong>")			
				ids = names[2].split("</strong>")
				if ids[0].find("FP=") > -1:
					fingers = line.split("FP=")
					for f in fingers:
						if (f[41] == '>'):
							print "PRINT "+ f[0:40]
				else:
					print "NAME " + ids[0]
			elif relay.find("<strong>Anonymous Relay"):
				print "ANON"
					
		#fingers = line.split("FP=")
		#for f in fingers:
		#	print f[0:40]				
finally:
	file.close()

	
