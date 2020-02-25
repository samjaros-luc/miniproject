import os

## Part 0: Clear log ##
log = open("miniProject.log","w")
log.close()

## Part 2: Make kallisto index ##
os.system("python3 buildKallisto.py")
