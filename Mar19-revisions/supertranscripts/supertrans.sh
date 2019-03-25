#!/bin/bash
#PBS -l ncpus=48	
#PBS -l mem=200gb
#PBS -l walltime=70:00:00
#PBS -M anna.kretzschmar@uts.edu.au
#PBS -m abe
#PBS -q c3b

module load devel/python-2.7.12
module load bio/Trinity-current
module load bio/hmmer-current


cd /shared/homes/125155/pant-transcriptomes/Mar19/supertranscripts

$TRINITY_HOME/Analysis/SuperTranscripts/Trinity_gene_splice_modeler.py --incl_malign --trinity_fasta /shared/homes/125155/pant-transcriptomes/poly/cawthron/output/Norm_Gambierdiscus-polynesiensis_CAWD254_comb.1.fastq.gz-assembly.fasta
