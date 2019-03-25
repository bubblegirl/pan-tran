#!/bin/bash
#PBS -l ncpus=30
#PBS -l mem=200gb
#PBS -l walltime=200:00:00
#PBS -M anna.kretzschmar@uts.edu.au
#PBS -m abe
#PBS -q c3b

module load bio/get_homologues-current

cd /shared/homes/125155/pant-transcriptomes/Mar19/get_hom-est 

get_homologues-est.pl -d alns -M -t=0 -c -z -n=25 
