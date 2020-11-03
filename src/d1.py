import sys
import os
import difflib

############################################  ALL THE DUAL ################################################
def percentage(fo1,fo2,diff):
   #calculating the difference between the two values
   if (fo2-fo1)>= diff:
       return 0
   else:
       return 1

#########

def ola(atom_lines1,atom_lines2,firstatom2,secondatom2,thirdatom2,fourthatom2,firstatom,secondatom,thirdatom,fourthatom,diff):
 p=0;l=0;sumA=0;sumB=0;n_linesA=0;n_linesB=0;n_lines=0
 m2=0;m=0;m3=0;sumA=0;sumB=0;divround=0;divabs=0
 name=[];name2=[]

 for a2 in range(atom_lines2):
    if secondatom2[a2] in secondatom :  #the two second words are the same so we have to check their values
      print("we are the same")
      m=fourthatom[a2]
      m=float(m)
      m2=fourthatom2[a2]
      m2=float(m2)
      print m,m2
      x = percentage(m,m2,diff)
      #print x
      if x == 1:  #they differ less than 10% so no need to do anything
            print("ouf")
            #stay as they are
      else:
            print("ta m einai")
            print (m,m2)
            print("oups") # the differ more than 0.1
            new.write("A %s " %(firstatom[a2]))
            new.write("%s " %(secondatom[a2]))
            name.append(secondatom[a2])
            new.write("%s " %(thirdatom[a2]))
            new.write("%s\n" %(fourthatom[a2]))
            sumA=sumA+m
            print("sumA",sumA)
            n_linesA=n_linesA+1 

            new.write("B %s " %(firstatom2[a2]))
            new.write("%s " %(secondatom2[a2]))
            name2.append(secondatom2[a2])
            new.write("%s " %(thirdatom2[a2]))
            new.write("%s\n" %(fourthatom2[a2]))
            sumB=sumB+m2
            print("sumB",sumB)
            n_linesB=n_linesB+1
      print(secondatom[a2])
    if secondatom2[a2] not in secondatom:

           print("dn einai reference")
           
           new.write("B %s " %(firstatom2[a2]))
           new.write("%s " %(secondatom2[a2]))
           name2.append(secondatom2[a2])
           new.write("%s " %(thirdatom2[a2]))
           new.write("%s\n" %(fourthatom2[a2]))
           fatom2=float(fourthatom2[a2])
           sumB=sumB+fatom2
           print("sumB",sumB)
           n_linesB=n_linesB+1

 for a in range(atom_lines1):
    if secondatom[a] not in secondatom2:
       print("dn einai mutant")
       new.write("A %s " %(firstatom[a]))
       new.write("%s " %(secondatom[a]))
       name.append(secondatom[a])
       new.write("%s " %(thirdatom[a]))
       new.write("%s\n" %(fourthatom[a]))
       fatom1=float(fourthatom[a])
       sumA=sumA+fatom1
       print("sumA",sumA)
       n_linesA=n_linesA+1
 n_lines=n_linesA+n_linesB
 print(n_lines)

 extra=[];extra2=[]

 for b in range (bondsum2):
    databond2 = bond2[b]
    databond2 = databond2.split()

    firstbond2.append(databond2[0])
    secondbond2.append(databond2[1])
    thirdbond2.append(databond2[2])

    sec2=secondbond2[b].strip()
    asec2=sec2[0]
    
    thir2=thirdbond2[b].strip()
    athir2=thir2[0]
	
    for i in range(len(name2)):
		print secondbond2[b], thirdbond2[b]
		if secondbond2[b]==name2[i]:
			if athir2 == 'H' and thirdbond2[b] not in name2:
				extra2.append(thirdbond2[b])
		if thirdbond2[b]==name2[i] and secondbond2[b] not in name2:
			if asec2=='H':
				extra2.append(secondbond2[b])
 
 for b in range (bondsum):
    databond = bond[b]
    databond = databond.split()
	
    firstbond.append(databond[0])
    
    secondbond.append(databond[1])
    thirdbond.append(databond[2])

    sec=secondbond[b].strip()
    asec=sec[0]
    
    thir=thirdbond[b].strip()
    athir=thir[0]

    for i in range(len(name)):               
        if secondbond[b]==name[i] and thirdbond[b] not in name:
            if athir == 'H':
              extra.append(thirdbond[b])
        if thirdbond[b]==name[i] and secondbond[b] not in name:
            if asec=='H':
              extra.append(secondbond[b])
 print(extra,extra2)
 extracharge=[];extracharge2=[]
 for i in range(len(extra)):
    for j in range(atom_lines1):
     if extra[i]==secondatom[j]:
      extracharge.append(fourthatom[j])
      fatom1=float(fourthatom[j])
      new.write("A %s " %(firstatom[j]))
      new.write("%s " %(secondatom[j]))
      new.write("%s " %(thirdatom[j]))
      new.write("%s\n" %(fourthatom[j]))
      print(fatom1)
      sumA=fatom1+sumA
 n_linesA=n_linesA+len(extra)

 for i in range(len(extra2)):
    for j in range(atom_lines2):
     if extra2[i]==secondatom2[j]:
      extracharge2.append(fourthatom2[j])
      fatom2=float(fourthatom2[j])
      new.write("B %s " %(firstatom2[j]))
      new.write("%s " %(secondatom2[j]))
      new.write("%s " %(thirdatom2[j]))
      new.write("%s\n" %(fourthatom2[j]))
      print(fatom2)
      sumB=fatom2+sumB
 n_linesB=n_linesB+len(extra2)
 n_lines=n_linesA+n_linesB
 print("edw eimai",n_lines)
 
 print(sumA)
 print(sumB)
 print(n_linesB)
 print(extracharge,extracharge2)
 value=sumB-sumA
 div=value/n_linesB
 print (div)
 divabs=abs(div)
 divround=round(divabs,2)
 print ("!!!", divround)

 if(divround>0.02):
   print ("div is too big")
   diff=diff-0.01
   print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",diff)
   new.write("\n")
   n_lines,div=ola(atom_lines1,atom_lines2,firstatom2,secondatom2,thirdatom2,fourthatom2,firstatom,secondatom,thirdatom,fourthatom,diff)
   
 else:
   print(n_lines,div)
   return(n_lines,div)
 print(n_lines,div)
 return(n_lines,div)

##########

def update_charges(n,chargaki):
  firstb=[];secondb=[];thirdb=[];fourthb=[];fifthb=[];B=[];batom=[]
  newfifthb=[]
  Bsum=0
  new = open('dothemath.txt','r')
  for line in (new.readlines() [-n:]):
     print(line)
     if line.startswith ('B'):
       Bsum=Bsum+1
       B.append(line)
       #print(line)
  for b in range(Bsum):
    datab= B[b]
    datab = datab.split()

    firstb.append(datab[0])
    secondb.append(datab[1])
    thirdb.append(datab[2])
    fourthb.append(datab[3])
    fifthb.append(datab[4])
    newfifthb.append(float(datab[4])+chargaki)
  print(newfifthb)
  return(thirdb,fourthb,newfifthb)

#####################################NEW NAMES MUTATIONS ONLY################################################

def change_names(thirdb):
	print ("edoooo", thirdb)
	three2=[];four2=[]; p=0; q=0; n=0
	for i in range(len(thirdb)):
		t=thirdb[i].strip()
		if len(t)==1:
			a=t[0]
			b=' '
			c=' '
		elif len(t)>2:
			a=t[0]
			b=t[1]
			c=t[2]
		elif len(t)==2 :
			c= ' '
			a=t[0]
			b=t[1]
		print a,b,c 
		if (b.isalpha()) == True and (c.isalpha()) == ' ':
			continue
		elif (b.isalpha()) == ' ' and (c.isalpha()) == ' ':
			continue
		elif (b.isalpha()) == False and (c.isalpha()) == ' ':
			continue
		elif (b.isalpha()) == False or (c.isalpha()) == False:
			if (c.isalpha()) == True:
				continue	
		elif (b.isalpha()) == False and (c.isalpha()) == False:	
				c=c+1
				if c>9:
					b=1+b
					c=0
        	if(c.isalpha()) == False:
				c=n
				c=c+1

		elif (b.isalpha()) == True and (c.isalpha()) == True:
			print("mpikame")
			b=p
			p=p+1
			if b>9:
				b=0
				c=q
				q=q+1
		
		a=str(a)
		b=str(b)
		c=str(c)
		ola=[a,b,c]	
		newt=''.join(str(v) for v in ola)
		three2.append(newt)
	print three2
	return(three2)
##############################################  HYBRID RTF  ###################################################

def new_atoms(firstatom2,three2,four2,five,firstmass2,secondmass2,thirdmass2,fourthmass2,fifthmass2,firstbond2,secondbond2,thirdbond2,
firstimpr2,secondimpr2,thirdimpr2,fourthimpr2,fifthimpr2):
	#ligandC = sys.argv[3]  
	with open("/var/www/html/reference.rtf", 'r') as f:

		with open("f.txt", "w") as f1:
		    lines=f.readlines()
		    for i in range(0,len(lines)):
		       line=lines[i]
		       if line.startswith('MASS'):			#kapou edw isws prpei na elegxw ta masses tou mut.
		            next=lines[i+1]
		            if next.startswith('RESI'):
		             f1.write(lines[i])
		             for i in range(len(secondmass2)):
		               f1.write("%s " %(firstmass2[i]))
		               f1.write("%s " %(secondmass2[i]))
		               f1.write("%s " %(thirdmass2[i]))
		               f1.write("%s " %(fourthmass2[i]))
		               f1.write("%s\n" %(fifthmass2[i]))
		            else:
		               f1.write(line)
		       elif line.startswith('ATOM'):
		            next=lines[i+1]
		            if next.startswith('BOND'):
		             f1.write(lines[i])
		             for i in range(len(three)):
		               f1.write("%s " %(firstatom2[i]))
		               f1.write("%s " %(three2[i]))
		               f1.write("%9s " %(four[i]))
		               f1.write("%6s\n" %(five[i]))
		            else:
		               f1.write(line)
		       elif line.startswith('BOND'):
		            next=lines[i+1]
		            if next.startswith('IMPR'):
		             f1.write(lines[i])
		             for i in range(len(secondbond2)):
		               f1.write("%s " %(firstbond2[i]))
		               f1.write("%s " %(secondbond2[i]))
		               f1.write("%4s\n" %(thirdbond2[i]))
		            else:
		               f1.write(line)
		       elif line.startswith('IMPR'):
		            next=lines[i+1]
		            if next.startswith('PATCH'):
		             f1.write(lines[i])
		             for i in range(len(secondimpr2)):
		               f1.write("%s " %(firstimpr2[i]))
		               f1.write("%s " %(secondimpr2[i]))
		               f1.write("%s " %(thirdimpr2[i]))
		               f1.write("%s " %(fourthimpr2[i]))
		               f1.write("%s\n" %(fifthimpr2[i]))
		            else:
		               f1.write(line)
		       else:
		           f1.write(line)
#global later
def later(ta,tb):
   #lateruse=[]
   global lateruse
   lateruse=[]
   for i in range(len(ta)):
    lateruse.append("A"+ta[i])
    #lateruse.append(ta[i])
   for i in range(len(tb)):
    lateruse.append("B"+tb[i])
    #lateruse.append(tb[i])
##################################################################################################

#################################################################################################
################################## main #########################################################
ligandB = sys.argv[2] 
ligandA = sys.argv[1] 
with open('/var/www/html/reference.rtf','r') as infile1:   ######ALLAZEIS EDWWW
	with open('/var/www/html/smutant.rtf','r') as infile2:             ######ALLAZEIS EDWWW auto pou exeis parei apo to merge2.py
		with open('dothemath.txt','w')as new:    ###edw mporeis na elegxeis poia atoma tha paroun meros:
 

			atom_lines1=0;atom_lines2=0;atom_lines=0

			mass=[];bond=[];impr=[];end=[];atom=[]
			masssum=0;bondsum=0;imprsum=0;endsum=0

			mass2=[];bond2=[];impr2=[];atom2=[]
			masssum2=0;bondsum2=0;imprsum2=0;

			#read the two rtf files 
			while True:
				line1 = infile1.readline().strip()   #this ligand we keep as it is. we change ligandB
				if line1.startswith('MASS'):
					masssum=masssum+1
					mass.append(line1)
				if line1.startswith('ATOM'):
					atom.append(line1)
					atom_lines1=atom_lines1+1
				if line1.startswith('BOND'):
					bondsum=bondsum+1
					bond.append(line1)
				if line1.startswith('IMPR'):
					imprsum=imprsum+1
					impr.append(line1)
				if line1 =='':
					break;

			while True:
				line2 = infile2.readline().strip()   #masses tou mut kalutera
				if line2.startswith('MASS'):
					masssum2=masssum2+1
					mass2.append(line2)
				if line2.startswith('ATOM'):
					atom2.append(line2)
					atom_lines2=atom_lines2+1
				if line2.startswith('BOND'):
					bondsum2=bondsum2+1
					bond2.append(line2)
				if line2.startswith('IMPR'):
					imprsum2=imprsum2+1
					impr2.append(line2)
				if line2 == '':
					break;

			#how many lines begin with the word ATOM
			atom_lines=atom_lines1 + atom_lines2 
			print (atom_lines)
			print (masssum)
			print (bondsum)
			print (imprsum)

			firstatom=[];secondatom=[];thirdatom=[];fourthatom=[]
			firstatom2=[];secondatom2=[];thirdatom2=[];fourthatom2=[]
			firstmass=[];secondmass=[];thirdmass=[];fourthmass=[];fifthmass=[]
			firstmass2=[];secondmass2=[];thirdmass2=[];fourthmass2=[];fifthmass2=[]
			firstbond2=[];secondbond2=[];thirdbond2=[]
			firstbond=[];secondbond=[];thirdbond=[]
			firstimpr=[];secondimpr=[];thirdimpr=[];fourthimpr=[];fifthimpr=[]
			firstimpr2=[];secondimpr2=[];thirdimpr2=[];fourthimpr2=[];fifthimpr2=[]
			for a in range(atom_lines1):
				dataatom = atom[a]
				dataatom = dataatom.split()

				firstatom.append(dataatom[0])
				secondatom.append(dataatom[1])
				thirdatom.append(dataatom[2])
				fourthatom.append(dataatom[3])

			for a2 in range(atom_lines2):
				dataatom2 = atom2[a2]
				dataatom2 = dataatom2.split()

				firstatom2.append(dataatom2[0])
				secondatom2.append(dataatom2[1])
				thirdatom2.append(dataatom2[2])
				fourthatom2.append(dataatom2[3])

			print(secondatom)
			print(secondatom2)
			oldthirdb=[];oldfourthb=[]
			diff=0.1
			lines,chargaki=ola(atom_lines1,atom_lines2,firstatom2,secondatom2,thirdatom2,fourthatom2,firstatom,secondatom,thirdatom,fourthatom,diff)
			new.close()
			chargaki=round(chargaki,2)
			three,four,five=update_charges(lines,chargaki)  ##adding the div to each charge
			
			three2=change_names(three)   ##giving new names to atoms
			later(three,three2)
			##add the new atoms to ligandArtf in order to create the hybrid.
			print("llllllllllllllllllllllllll",three)

			####################################### mass #################################################
			i=0
			p=0
			print ("to 444444444", four)
			firstmass22=[];secondmass22=[];thirdmass22=[];fourthmass22=[];fifthmass22=[];
			for m in range(masssum2):
				datamass2 = mass2[m]
				datamass2 = datamass2.split()
				firstmass2.append(datamass2[0])
				secondmass2.append(datamass2[1])
				fourthmass2.append(datamass2[3])
				fifthmass2.append(datamass2[4])
				thirdmass2.append(datamass2[2])
				if thirdmass2[m]in four:
				 
				 for i in range(len(four)):
				  if thirdmass2[m]== four[i]:
				   if thirdmass2[m] not in thirdmass22:
				   	thirdmass22.append(four[i])
				   	p=p+1
				  
				   	secondmass22.append(datamass2[1])
				   	print ("mpika reeeeeee", secondmass22)
				   	firstmass22.append(datamass2[0])
				   	fourthmass22.append(datamass2[3])###peirazei i seiroula?
				   	fifthmass22.append(datamass2[4])###
				   
				   #print(firstmass22,secondmass22,thirdmass22,fourthmass22,fifthmass22)
			####################################### bond #################################################
			firstbond22=[];secondbond22=[];thirdbond22=[]
			for b in range (bondsum2):
				databond2 = bond2[b]
				databond2 = databond2.split()

				firstbond2.append(databond2[0])
				secondbond2.append(databond2[1])
				thirdbond2.append(databond2[2]) 


				if secondbond2[b] in three and thirdbond2[b] in three : 
					for i in range(len(three)):
					 if thirdbond2[b]==three[i]:
					   thirdbond22.append(three2[i]) 
				 
					 if secondbond2[b]==three[i]:
					   firstbond22.append(databond2[0])
					   secondbond22.append(three2[i]) 

				else: 
					for i in range(len(three)):
					 if thirdbond2[b]==three[i]:
					   firstbond22.append(databond2[0])
					   secondbond22.append(databond2[1])
					   thirdbond22.append(three2[i]) 
				 
					 if secondbond2[b]==three[i]:
					   firstbond22.append(databond2[0])
					   secondbond22.append(three2[i])
					   thirdbond22.append(databond2[2]) 
			#print(firstbond22,secondbond22,thirdbond22)

			####################################### impr #################################################
			firstimpr22=[];secondimpr22=[];thirdimpr22=[];fourthimpr22=[];fifthimpr22=[]

			for im in range (imprsum2):
		
				dataimpr2 = impr2[im]
				dataimpr2 = dataimpr2.split()

				firstimpr2.append(dataimpr2[0])
				secondimpr2.append(dataimpr2[1])
				thirdimpr2.append(dataimpr2[2])
				fourthimpr2.append(dataimpr2[3])
				fifthimpr2.append(dataimpr2[4])

				if secondimpr2[im] in three and thirdimpr2[im] in three and fourthimpr2[im] in three and fifthimpr2[im] in three: 
					print("mpainei edw kale? mpaaaa")
					for i in range(len(three)):
					 if thirdimpr2[im]==three[i]:
					   thirdimpr22.append(three2[i]) 
				 
					 if secondimpr2[im]==three[i]:
					   firstimpr22.append(dataimpr2[0])
					   secondimpr22.append(three2[i]) 
					 
					 if fourthimpr2[im]==three[i]:
						fourthimpr22.append(three2[i])

					 if fifthimpr2[im]==three[i]:
						fifthimpr22.append(three2[i])
		
				if secondimpr2[im] in three or thirdimpr2[im] in three or fourthimpr2[im] in three or fifthimpr2[im] in three: 
				
				  print("mpainei edw kale? naiiii")
				  firstimpr22.append(dataimpr2[0])

				  if secondimpr2[im] in three:
					for i in range(len(three)):
					  if secondimpr2[im] == three[i]:
					   secondimpr22.append(three2[i])    
				  else:
						secondimpr22.append(dataimpr2[1])
				  
				  if thirdimpr2[im] in three:
					for i in range(len(three)):
					 if thirdimpr2[im] == three[i]:
					   thirdimpr22.append(three2[i])    
				  else:
						thirdimpr22.append(dataimpr2[2])
					   
				  if fourthimpr2[im] in three:
					for i in range(len(three)):
					  if fourthimpr2[im] == three[i]:
					   fourthimpr22.append(three2[i])           
				  else:
						fourthimpr22.append(dataimpr2[3])

				  if fifthimpr2[im] in three:
					for i in range(len(three)):
					 if fifthimpr2[im] == three[i]:
					   fifthimpr22.append(three2[i])
				  else:       
						 fifthimpr22.append(dataimpr2[4])

				
			print(firstimpr22,secondimpr22,thirdimpr22,fourthimpr22,fifthimpr22)
			new_atoms(firstatom2,three2,four,five,firstmass22,secondmass22,thirdmass22,fourthmass22,fifthmass22,firstbond22,secondbond22,
			thirdbond22,firstimpr22,secondimpr22,thirdimpr22,fourthimpr22,fifthimpr22)

			lines_seen = set() # holds lines already seen
			outfile = open("final.txt", "w")
			for line in open("f.txt", "r"):
			    if line not in lines_seen: # not a duplicate
				outfile.write(line)
				lines_seen.add(line)
			outfile.close()      

