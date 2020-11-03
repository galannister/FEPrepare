import sys
import os
import difflib

filein = sys.argv[1]


with open('reference.str', 'w') as outfile:
	with open(filein, 'r') as infile:
		always_print = False
		lines= infile.readlines()
		    
		for line in lines:
  			if always_print or "read param" in line:
     				print line
     				outfile.write(line)
     				always_print = True
