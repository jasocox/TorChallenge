import os
import sys
import re

file = open(sys.argv[1],'r')

try:
	myprints = []
	for line in file:
		fingers = line.split("FP=")
		for f in fingers:
			if (f[41] == '>'):
				fp = f[0:40]
				if (fp.isalnum()):
					myprints.append(fp)
	for p in myprints:
		print p
	
finally:
	file.close()	
