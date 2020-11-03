import sys
import os
import difflib

reflig=[]; mutlig=[]; mutant=[]; outputlist=[]; linesmut=[]; linesref=[]; decl=[]; resi=[]; impr=[]; bond=[]; atomindex=[]; sortedatoms=[]; atomlines=[]; totallines=[]; referencelines=[]; mutligands=[];


def mutantFinder(mutlig, reflig, mutant,atomlines):
	for i in range(0,len(mutlig)):
		if mutlig[i] not in reflig:		#find mutation (//reflig[i] in mutlig and )
			mutant.append(atomlines[i])
	return mutant

		

with open('reference.rtf','r') as infile1:
	with open('mutant.rtf','r') as infile2:
		with open ('smutant.rtf','w') as outfile: 	
			linesref= infile1.readlines()     			#get all atoms from both files
			linesmut= infile2.readlines()
			x=len(linesref)
			y=len(linesmut)
			
			for i in range(x,y):
				linesref.append(" ")
			for i in range(0, len(linesref)):
				totallines.append(linesmut[i])		
				lineref =linesref[i]
				atomref=lineref.split()
				linemut=linesmut[i]		
				atommut=linemut.split()	

				if lineref.startswith('ATOM'):			#WRITE ref and mut names in separate lists
					referencelines.append(lineref)
					reflig.append(atomref[1])
			
				if linemut.startswith('ATOM'):
					atomlines.append(linemut)
					mutlig.append(atommut[1])
				q=len(mutlig)
				p=len(reflig)
			
			for i in range(p,q):
				reflig.append(" ")
				referencelines.append(" ")
			#print atomlines, mutlig
		
			mutantFinder(mutlig, reflig, mutant,atomlines)	
			for i in range(0,len(mutlig)):
				if reflig[i] in mutlig and reflig[i]!= ' ':							#if mutant in reference write mutant in the correct position
					
					kati=mutlig.index(reflig[i])					#pes mou pou irarxei to mut[i] sto ref arxeio
				
					#corrpos=mutlig.index(reflig[kati])							#pes mou pou iparxei sto mut to ref m ayto to onoma	kai tipose to

					outputlist.append(atomlines[kati])
					
				


				if reflig[i] not in mutlig:
					x=mutant.pop(0)
					outputlist.append(x)

				cnt=0
			for i in range(0,len(outputlist)-1):
				empty=outputlist[i]
				if empty== " ":
					cnt=cnt+1
			for i in range(0,len(outputlist)-cnt):
				empty=outputlist[i]
				if empty== " ":		
					outputlist.pop(i)										
					
			if not mutant:
				for i in range(0,len(mutant)):
                  
					x=mutant.pop(0)
					outputlist.append(x)				
			
		

			for i in range(0, len(totallines)):
				atmlines=totallines[i]
				if atmlines.startswith('*' or '!'):
					outfile.write(atmlines)
				if atmlines.startswith('read rtf'):
					outfile.write(atmlines)
				if atmlines.startswith('36 1'):
					outfile.write(atmlines)
				if atmlines.startswith('MASS'):
					outfile.write(atmlines)
				
				
				
					
				
				#if atmlines.startswith('DECL'):
				#	decl.append(atmlines)
				if atmlines.startswith('RESI'):
					resi.append(atmlines)
					
					
				if atmlines.startswith('IMPR'):
					if atmlines.startswith('IMPROPERS'):
						continue
					impr.append(atmlines)
				if atmlines.startswith('BOND'):
					if atmlines.startswith('BONDS'):
						continue
					bond.append(atmlines)
			for k in range(0, len(resi)):
				outfile.write(resi[k])	
			for i in range(0,len(outputlist)):
				srtatoms=outputlist[i];
				outfile.write(srtatoms)
			#for b in range(0, len(decl)):
			#	dcl=decl[b]
			#	outfile.write(dcl)
			
			for c in range(0, len(bond)):
				bnd=bond[c]
				outfile.write(bnd)
			for i in range(0, len(impr)):
				outfile.write(impr[i])

			outfile.write("\nEND")


		#ratoms=rline.split()
		#			ratom=ratoms[1]
		#			for i in range(0,len(atomlines)):
		#				splitmuts=atomlines[i].split()
		#				splitmut=splitmuts[1]
		#				if ratom==splitmuts:
		#					outputlist.append(atomlines[i])
				
