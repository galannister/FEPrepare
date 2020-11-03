import sys
import os
import difflib

fileref = sys.argv[1]
filemut = sys.argv[2]

mutcheck=[]; cnt=0
with open('/var/www/html/ligand.pdb', 'w') as outfile:
	with open(fileref, 'r') as infile1: 
		with open(filemut, 'r') as infile2: 
			   
			lines= infile1.readlines()
			mutlines=infile2.readlines()
			for i in range(0,len(lines)):
				line = lines[i]
				data = line.split()
				if line.startswith('ATOM') or line.startswith('HETATM'):
					outfile.write(line)
					mutcheck.append(data[2])
					hybnum=int(data[1])	
			for i in range(0,len(lines)):
				mline = mutlines[i]
				mdata = mline.split()
				if mline.startswith('ATOM') or mline.startswith('HETATM'):
					if mdata[2] not in mutcheck:
						print hybnum, mdata[1]
						m=int(mdata[1])
						name=mdata[2]
						names=list(name)
						mdata[1]= hybnum+1+cnt
						cnt=cnt+1
						outfile.write("%s " %(mdata[0])) 
						print len(names),name
						if len(names)<3:
							print("mpike edw 1")
							outfile.write("%4s " %(mdata[1]))
							outfile.write("%3s " %(mdata[2]))
							outfile.write("%4s " %(mdata[3]))
							outfile.write("%5s " %(mdata[4]))
							outfile.write("%11s " %(mdata[5]))
							outfile.write("%7s " %(mdata[6]))
							outfile.write("%7s " %(mdata[7]))
							outfile.write("%5s " %(mdata[8]))
							outfile.write("%5s " %(mdata[9]))
							outfile.write("%11s \n" %(mdata[10]))
						if len(names)==3:
							print("mpike edw 2")
							outfile.write("%4s " %(mdata[1]))
							outfile.write("%4s " %(mdata[2]))
							outfile.write("%3s " %(mdata[3]))
							outfile.write("%5s " %(mdata[4]))
							outfile.write("%11s " %(mdata[5]))
							outfile.write("%7s " %(mdata[6]))
							outfile.write("%7s " %(mdata[7]))
							outfile.write("%5s " %(mdata[8]))
							outfile.write("%5s " %(mdata[9]))
							outfile.write("%11s \n" %(mdata[10]))
						if len(names)>3:
							outfile.write("%3s " %(mdata[1]))
							outfile.write("%4s " %(mdata[2]))
							outfile.write("%4s " %(mdata[3]))
							outfile.write("%5s " %(mdata[4]))
							outfile.write("%11s " %(mdata[5]))
							outfile.write("%7s " %(mdata[6]))
							outfile.write("%7s " %(mdata[7]))
							outfile.write("%5s " %(mdata[8]))
							outfile.write("%5s " %(mdata[9]))
							outfile.write("%11s \n" %(mdata[10]))
						
