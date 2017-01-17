# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 22:20:34 2015

@author: Vinay
"""
from __future__ import division
import nltk
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from nltk.tokenize import word_tokenize
IN = open("D:\\SMM\\Project\\Speeches\\DonaldTrump\\Donald_Trump_Commencement.txt")

text = IN.read()
print text
text= text.lower() # Normalizing the text
    
length= len(text)
unique= sorted(set(text)) # The vocabulary of a text is just the set of tokens that it uses, since in a set, all duplicates are collapsed together
unique_words= len(unique)
lexical_richness= (unique_words/length)* 100
new=word_tokenize(text)
tagged = nltk.pos_tag(new)
print length # gets the entire vocabulary items
print unique_words
print lexical_richness
    
 
holder=[]

for a,b in tagged:
    if( b=="NNP" or b=="NN" or b=="JJ"):
        holder.append(a)
   

f = open("D:\\SMM\\Project\\Speeches\\DonaldTrump\\POSDonald.txt",'w')
for i in holder:
    f.write(i+'\n'),
f.close()

       

