#!/bin/bash
#PBS -l ncpus=48	
#PBS -l mem=200gb
#PBS -l walltime=150:00:00
#PBS -M anna.kretzschmar@uts.edu.au
#PBS -m abe
#PBS -q c3b

module load bio/TransDecoder-current

cd /shared/homes/125155/pant-transcriptomes/Mar19/supertranscripts/1-processing

TransDecoder.LongOrfs -t CAWD254_Gambierdiscus-polynesiensis_supertrans.fasta
TransDecoder.Predict -t CAWD254_Gambierdiscus-polynesiensis_supertrans.fasta

TransDecoder.LongOrfs -t CG15_Gambierdiscus-polynesiensis_supertrans.fasta
TransDecoder.Predict -t CG15_Gambierdiscus-polynesiensis_supertrans.fasta

TransDecoder.LongOrfs -t HG4_Gambierdiscus-lapillus_supertrans.fasta
TransDecoder.Predict -t HG4_Gambierdiscus-lapillus_supertrans.fasta

TransDecoder.LongOrfs -t HG5_Gambierdiscus-silvae_supertrans.fasta
TransDecoder.Predict -t HG5_Gambierdiscus-silvae_supertrans.fasta

TransDecoder.LongOrfs -t MMETSP0766_Gambierdiscus-australes_supertrans.fasta
TransDecoder.Predict -t MMETSP0766_Gambierdiscus-australes_supertrans.fasta

TransDecoder.LongOrfs -t UTSMER9A_Gambierdiscus-carpenteri_supertrans.fasta
TransDecoder.Predict -t UTSMER9A_Gambierdiscus-carpenteri_supertrans.fasta
