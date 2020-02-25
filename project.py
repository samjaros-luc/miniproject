import os

## Part 0: Clear log ##
log = open("miniProject.log","w")
log.close()

## Part 2: Make kallisto index ##
os.system("python3 buildKallisto.py")

## Part 3: Determine TPM for each CDS ##
os.system("Rscript runSleuth.R")

## Part 4: Align with Bowtie2 ##
os.system("python3 alignBowtie.py")

## Part 5: Assemble with SPAdes ##
os.system("python3 assembleSPAdes.py")

## Parts 6-8: Get contigs of >1000 bp and concatenate them ##
os.system("python3 1000contigs.py")


