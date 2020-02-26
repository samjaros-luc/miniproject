import os
from Bio import Entrez,SeqIO
import subprocess

## Open log to write to ##
log = open("miniProject.log","a")

# Method for counting lines in file taken off stackoverflow
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i+1

# Step 1: Get .fasta of the whole genome
ID = "EF999921"
Entrez.email = "sam.jaros.sj@gmail.com"
handle = Entrez.efetch(db="nuccore", id=ID, rettype="gb") # get the genbank entry
seq = ""
for record in SeqIO.parse(handle, "genbank"): # converts the generator object into a record
    seq = ">"+record.id+"\n"+str(record.seq)
fileOut = open("results/EF999921.fasta","w")
fileOut.write(seq)
handle.close()
fileOut.close()

# Step 2: Build bowtie2 index
os.system("bowtie2-build results/EF999921.fasta results/hh5/hh5")

# Step 3: Allign reads with index
seqNames = os.listdir("data")
for file in seqNames:
    os.system("bowtie2 -x results/hh5/hh5 -1 data/"+file+"/"+file+"_1.fastq -2 data/"+file+"/"+file+"_2.fastq --al-conc results/"+file+"/"+file+".fastq --no-unal -S results/"+file+"/"+file+".sam")
    # Step 4: Write to the output
    if file == "SRR5660030.1":
        log.write("Donor 1 (2dpi)")
    elif file == "SRR5660033.1":
        log.write("Donor 1 (6dpi)")
    elif file == "SRR5660044.1":
        log.write("Donor 3 (2dpi)")
    elif file == "SRR5660045.1":
        log.write("Donor 3 (6dpi)")
    numStart = file_len("data/"+file+"/"+file+"_1.fastq")/4
    numEnd = file_len("results/"+file+"/"+file+".1.fastq")/4
    log.write("had "+str(numStart)+" read pairs before Bowtie2 filtering and "+str(numEnd)+" read pairs after.\n")

log.close()
