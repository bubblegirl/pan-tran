#!/bin/bash
#PBS -l ncpus=30
#PBS -l mem=200gb
#PBS -l walltime=200:00:00
#PBS -M anna.kretzschmar@uts.edu.au
#PBS -m abe
#PBS -q c3b

module load bio/get_homologues

cd /shared/homes/125155/pant-transcriptomes/Mar19/supertranscripts/2B-get_hom 

get_homologues.pl -M -t 0 -d fasties
