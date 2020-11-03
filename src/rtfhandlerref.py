import sys
import os
import difflib


stratom=[]; strmass=[]; strdecl=[]; strresi=[]; strbond=[];strparsing=[];labels=[]; stratomline=[]; massdata=[];impr=[];
filein = sys.argv[1]

pdb= sys.argv[2]
with open(pdb, 'r') as pdbreader:
	pdblines=pdbreader.readlines()
	for i in range(0,len(pdblines)):
			pdbline = pdblines[i]
			pdbdata = pdbline.split()
			if pdbline.startswith('HETATM') or pdbline.startswith('ATOM') :
				resiname= pdbdata[3]
									
				


with open('reference.rtf', 'w') as outfile:
	with open(filein, 'r') as infile: #DOSE apo cmd 
		with open('/var/www/html/Std_Masses.txt', 'r') as infile2:
			
			lines= infile.readlines()
		       

			for i in range(0,len(lines)):
				line = lines[i]
				data = line.split()
				


				if line.startswith('*' or '!'):
					outfile.write(line)
				if line.startswith('read rtf'):
					outfile.write(line)
				if line.startswith('ATOM'):
					stratom.append(data[2])
					stratomline.append(line)
				if line.startswith('RESI'):
					print data[9], data[10]
					resiline=data[0]+ ' ' + resiname + ' ' + data[2] + ' '+ data[3] + ' ' + data[4] + ' ' + data[5] + ' ' + data[6] + ' ' + data[7]+ ' ' + data[8]+ ' ' + data[9] + data[10] + '\n'	
									
					strresi.append(resiline)
				if line.startswith('DECL'):
					strdecl.append(line)
			

					outfile.write("36 1 \n")
				if line.startswith('IMPR '):
					if line.startswith('IMPROPERS'):
						continue
					impr.append(line)
				if line.startswith('BOND'):
					if line.startswith('BONDS'):
						continue	
					strbond.append(line)


			
			for l in range(0,3):
				
				masslines= infile2.readlines()
			
			for l in range(0,len(stratom)):
				
				stratomsplit=list(stratom[l])

				if stratomsplit[0] == 'C' and stratomsplit[1] == 'G':
	 #or stratomsplit[0] == 'C' and stratomsplit[1] != 'E' or stratomsplit[0] == 'C' and stratomsplit[2]!= 'L' :
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'C':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))
		#C
				
				if stratomsplit[0] == 'C' and stratomsplit[1] == 'L':
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'CL':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))	
	
		#cl
				if stratomsplit[0] == 'C' and stratomsplit[1] == 'E' and stratomsplit[2] == 'S' :
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'CES':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))	
		#CES

				if stratomsplit[0] == 'C' and stratomsplit[1] == 'A' and stratomsplit[2] == 'L' :
					for j in range(0, len(masslines)-2):
						massline = masslines[j]
						massdata = massline.split()
					if massdata[2] == 'CAL':
						massdata[2] = stratom[l]
						outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))	

	#cal
	

				if stratomsplit[0] == 'H':
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'H':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))	
							
#H						
				if stratomsplit[0] == 'N':
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'N':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))	
	#N
				if stratomsplit[0] == 'O':
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'O':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))
	#O

				if stratomsplit[0] == 'S' and stratomsplit[1] != 'O' or stratomsplit[0] == 'S' and stratomsplit[2] != 'D' :
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'S':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))
	#S

				if stratomsplit[0] == 'S' and stratomsplit[1] == 'O' and stratomsplit[2] =='D' :
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'SOD':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))
	#SOD

				if stratomsplit[0] == 'M' and stratomsplit[1] == 'G':
					for j in range (0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'MG':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))
	#MG

				if stratomsplit[0] == 'P' and stratomsplit[1]== 'O' and stratomsplit[2] == 'T' :
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'POT':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))
	#pot

				if stratomsplit[0] == 'P':
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'P':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))
	#P


				if stratomsplit[0] == 'F':
					for j in range(0, len(masslines)):
						massline = masslines[j]
						massdata = massline.split()
						if massdata[2] == 'F':
							massdata[2] = stratom[l]
							outfile.write("%s %s %s %s %s \n" %(massdata[0], massdata[1], massdata[2], massdata[3], massdata[4]))
				
	#F		
			
		
			for b in range(0, len(strdecl)):
				outfile.write("%s" %(strdecl[b]))
			for k in range(0, len(strresi)):
				outfile.write("%s" %(strresi[k]))	
			for a in range(0, len(stratomline)):
				outfile.write('%s' %(stratomline[a]))
			for c in range(0, len(strbond)):
				outfile.write("%s" %(strbond[c]))
			for i in range(0, len(impr)):
				outfile.write("%s" %(impr[i]))
 			
			outfile.write("END\n")
					
				
