#!/bin/bash
#PBS -l ncpus=15	
#PBS -l mem=50gb
#PBS -l walltime=50:00:00
#PBS -M anna.kretzschmar@uts.edu.au
#PBS -m abe
#PBS -q c3b

module load bio/hmmer-3.1b2 

cd /shared/homes/125155/pant-transcriptomes/Mar19/supertranscripts/3-dinoSL

gunzip CG15_Gambierdiscus-polynesiensis_comb.2.fastq.gz

sed -n '1~4s/^@/>/p;2~4p' CG15_Gambierdiscus-polynesiensis_comb.2.fastq > CG15_Gambierdiscus-polynesiensis_comb.2.fasta

/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmsearch --tblout CG15_Gambierdiscus-polynesiensis_2_dinoSL.tbl dinoSL.hmm CG15_Gambierdiscus-polynesiensis_comb.2.fasta

/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/esl-sfetch --index CG15_Gambierdiscus-polynesiensis_comb.2.fasta

grep -v "^#" CG15_Gambierdiscus-polynesiensis_2_dinoSL.tbl | awk '{print $1}' | /shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/esl-sfetch -f CG15_Gambierdiscus-polynesiensis_comb.2.fasta - > CG15_Gambierdiscus-polynesiensis_2_dinoSL.fa
#/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmsearch --tblout CG15_Gambierdiscus-polynesiensis_comb.1.fastq.tbl dinoSL.hmm CG15_Gambierdiscus-polynesiensis_comb.1.fastq 

#/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/esl-sfetch --index CG15_Gambierdiscus-polynesiensis_comb.1.fastq

#grep -v \"^#\" CG15_Gambierdiscus-polynesiensis_comb.1.fastq.tbl | gawk \'{print $1}\' | /shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/esl-sfetch -f CG15_Gambierdiscus-polynesiensis_comb.1.fastq -> CG15_Gambierdiscus-polynesiensis_comb.1.fastq.dinoSL.fa
