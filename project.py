import os

## Part 0: Clear log ##
log = open("miniProject.log","w")
log.close()

## Part 2: Make kallisto index ##
os.system("python3 buildKallisto.py")

## Part 3: Determine TPM for each CDS
os.system("Rscript runSleuth.R")


