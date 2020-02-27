# miniproject
Mini-project for Dr. Wheeler's COMP 383

Author: Sam Jaros

# Software Requirements
- Linux
- Python 3.0 or later
- R
## Additional dependencies which must be installed and in the PATH:
- [Biopython](https://biopython.org/)
- [kallisto](https://pachterlab.github.io/kallisto/)
- [sleuth](https://pachterlab.github.io/sleuth/)
- [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)
- [SPAdes](http://cab.spbu.ru/software/spades/)

# Scripts
- project.py
  - Primary "runner" file
  - Will call the other scripts in the appropriate order given the input data is properly placed in `data`
- buildKallisto.py
  - Fetches NCBI:EF999921, takes the CDS, and builds the kallisto index
  - For every read pair, it quanifies the TPM using the kallisto index
- runSleuth.R
  - Tests for differential expression between 2dpi and 6dpi on the two patients
- alignBowtie.py
  - Builds bowtie2 index from NCBI:EF999921
  - For each read pair, takes only reads that map back to the reference genome
- assembleSPAdes.py
  - Assembles reads into contigs
- 1000contigs.py
  - Concatenates all contigs of length greater than 1000bp
- blastSeq.py
  - Blasts the sequence against the NCBI curated nucleotide database only of the *Herpesviridae* family
- miniProject.log
  - Contains information from each of the above scripts specified on the assignment sheet

# Directories
- data
  - Contains the raw read pairs
  - Must be in this format:
    - A series of top level folders
    - Each top level folder with name [name] must contain at least two paired end read files: [name]_1.fastq and [name]_2.fastq
- results
  - Is built by `project.py`
  - Contains the output from all of the above tools
