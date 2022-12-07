#!/usr/bin/env python
# coding: utf-8

# # Parsing Fasta File
# ## By: Molly Davis

# Write a python code with arguments that takes this file.fasta as input.
# It must count the length of the seq string, the number of 'A,T,G,C' only also the number of possible dinucleotides (for example AT, CT etc).

# In[4]:


from Bio.Seq import Seq
from Bio import SeqIO
file= list(SeqIO.parse("/Users/mollydavis333/desktop/file.fasta", "fasta"))
for sequence in file:
    print(sequence.id)
    print("Original Sequence:", sequence.seq)
    bases= ["A", "T", "G", "C"]
    seq=[]
    for i in sequence.seq.upper():
        if (i in bases):
            seq.append(i)
            
    print("Sequence Length:",len(seq))
    print("A Count:",seq.count("A"))
    print("T Count:",seq.count("T"))
    print("G Count:",seq.count("G"))
    print("C Count:",seq.count("C"))
    
    dinucleotides= ["AT", "CT", "GT", "TT", 
                    "AA", "CA", "GA", "TA", 
                    "GG", "AG", "CG", "TG", 
                    "AC", "CC", "GC", "TC"]
    
    dna= sequence.seq.upper()
    all_dinucs=[]
    for dinucleotide in dinucleotides:
        count= dna.count(dinucleotide) 
        #print("Count is " + str(count) + " for " + dinucleotide) ##can print to check to see each Dinuc amount
        all_dinucs.append(count)
        
    print("Number of Possible Dinucleotides:",sum(all_dinucs))

    print("-------------------------------------")
    

