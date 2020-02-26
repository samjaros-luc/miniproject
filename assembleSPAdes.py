import os

log = open("miniProject.log","a")

## Part 4: Run spades on Bowtie output ##
command = "spades.py --disable-gzip-output --only-assembler " # beginning of command
index = 1
for file in os.listdir("data"):
    # create input section of spades command
    command += "--pe"+str(index)+"-1 results/"+file+"/"+file+".1.fastq --pe"+str(index)+"-2 results/"+file+"/"+file+".2.fastq "
    index += 1
command += "-o results/SPAdes" # output section of spades command
os.system(command) # run the command
log.write(command+"\n") # log the command
log.close()
