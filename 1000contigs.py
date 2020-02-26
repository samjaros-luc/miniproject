import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_nucleotide

log = open("miniProject.log","a")

## Part 6: Get the contigs >1000bp ##
over1000 = [record for record in SeqIO.parse(open("results/SPAdes/contigs.fasta"),"fasta") if len(record)>1000]
log.write("There are "+str(len(over1000))+" contigs > 1000 bp in the assembly.\n")
SeqIO.write(over1000, "results/1000contigs.fasta", "fasta")

## Part 7: Get total length of the contigs ##
totalLength = 0
for record in over1000:
    totalLength += len(record.seq)
log.write("There are "+str(totalLength)+" bp in the assembly.\n")

## Part 8: Concatenate contigs ##
Ns = "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
seqs = []
for record in over1000:
    seqs.append(str(record.seq))
concat = SeqRecord(Seq(Ns.join(seqs),generic_nucleotide),id="Concatenated contigs",description="Concatenated contigs with N[50] between each contig")
SeqIO.write(concat, "results/concat.fasta", "fasta")


