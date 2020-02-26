from Bio import SeqIO
from Bio.Blast import NCBIWWW,NCBIXML

log = open("miniProject.log","a")

## Part 9: BLAST concatenated contigs ##
concatContig = open("results/1000contigs.fasta","r").read() # grab the concatenated fasta
# blastn with the concatContig through the curated nucleotide database looking for only the top 10 hits searching through the Herpesviridae family
resultHandle = NCBIWWW.qblast("blastn", "nr", concatContig, hitlist_size=10, entrez_query="Herpesviridae[Organism]")
blastRecords = NCBIXML.parse(resultHandle) # get records
blastRecord = next(blastRecords) # get the first record (there should only be one)

top10 = "seq_title\tallign_len\tnumber_HSPs\ttopHSP_ident\ttopHSP_gaps\ttopHSP_bits\ttopHSP_expect\n" # create headers
for alignment in blastRecord.alignments: # for each of the 10 alignments, grab the information needed
    top10 += alignment.title+"\t"+str(alignment.length)+"\t"+str(len(alignment.hsps))+"\t"+str(alignment.hsps[0].identities)+"\t"+str(alignment.hsps[0].gaps)+"\t"+str(alignment.hsps[0].bits)+"\t"+str(alignment.hsps[0].expect)+"\n"

log.write(top10)

log.close()
resultHandle.close()
