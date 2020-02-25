import os
from Bio import Entrez,SeqIO

## Part 0: Set up log ##
log = open("miniProject.log","w")

## Part 2: Make kallisto index ##
# Step 1: Get CDSs as a .fasta in the data folder
ID = "EF999921"
Entrez.email = "sam.jaros.sj@gmail.com"
handle = Entrez.efetch(db="nuccore", id=ID, rettype="gb") # get the genbank entry
numCDSs = 0
CDSs = ""
for record in SeqIO.parse(handle, "genbank"): # converts the generator object into a record
    for feature in record.features: # look through features of the genbank entry
        if feature.type == "CDS": # if the feature is a CDS, add it to the list and add to the count
            CDSs += ">"+feature.type+str(feature.location)+"\n"+str(feature.extract(record.seq))+"\n"
            numCDSs += 1
log.write("The HCMV genome (" + ID + ") has " + str(numCDSs) + " CDS.") # log the reqirued data
fileOut = open("data/EF999921_CDS.fasta","w") # write the CDSs to the appropriate file
fileOut.write(CDSs)
handle.close()
fileOut.close()

#Step 2: Index with kallisto
os.system("kallisto index -i data/EF999921.idx --make-unique data/EF999921_CDS.fasta") # use default k=31 b/c reads are long

## All done! ##
log.close()
