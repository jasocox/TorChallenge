import os
import sys
import re
import string

def ishex(s):
  for c in s:
    if not c in string.hexdigits: return False

  return True

file = open(sys.argv[1],'r')

try:
	myprints = []
	for line in file:
		fingers = line.split("FP=")
		for f in fingers:
			if (f[41] == '>'):
				fp = f[0:40]
				if (ishex(fp)):
					myprints.append(fp)
	for p in myprints:
		print p
	
finally:
	file.close()	

