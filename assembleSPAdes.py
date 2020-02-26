import os

# Open log file
log = open("miniProject.log","a")


## Part 4: Run spades on Bowtie output ##
command = "spades.py --disable-gzip-output --only-assembler "
index = 1
for file in os.listdir("data"):
    # assemble spades command, no need to zip output, only assemble the sequences, index defines each pair of reads
    command += "--pe"+str(index)+"-1 results/"+file+"/"+file+".1.fastq --pe"+str(index)+"-2 results/"+file+"/"+file+".2.fastq "
    index += 1
command += "-o results/SPAdes"
os.system(command) # run the command
log.write(command+"\n") # log the command
log.close()
