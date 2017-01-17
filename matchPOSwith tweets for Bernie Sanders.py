# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:41:41 2015

@author: Vinay
"""
lookup=[]
match=[]
IN= open("D:\\SMM\\Project\\Speeches\\Bernie_Sanders\\POSBernie.txt")
line="XXX"
while line:
 line=IN.readline().rstrip("\n")
 lookup.append(line)

txt= open("D:\SMM\Project\Speeches\opp.txt")
newline="RTR"
while  newline :
    newline=txt.readline().lower()
    new= newline.split()
    for i in lookup:
        if i in new:
            match.append(i)
        
print "Done"
print (match)

f = open("D:\SMM\Project\Speeches\BernieSanders_positivematches.txt",'w')
for i in match:
    f.write(i+" ")
f.close()

print "This is the length of POS words " + str(len(lookup))

print "This is total count match "+ str (len(match))

print "This is unique count match " +str(len(set(match)))






    


