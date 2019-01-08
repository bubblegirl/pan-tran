#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

def hmmaln1(): #use hmmer to extract correct ORF for fastafiles and align
	for file in glob('/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/*_assembly.fasta'): #fasta files w all 6 ORFs of protein files
		stat = file.split(".")[0] #get busco ID
		ernd = file.split(".")[1]
		cluster = stat + "." + ernd
		with open(file, 'r'):
#			build_lib = "/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmbuild dinoSL.hmm dinoSL.sto"
			search_cmd = "/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmsearch --tblout " + cluster + ".tbl dinoSL.hmm " + cluster
			index_cmd = "/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/esl-sfetch --index " + cluster
			extr_cmd = "grep -v \"^#\" " + cluster + ".tbl | gawk \'{print $1}\' | /shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/esl-sfetch -f " + cluster + " -> " + cluster + "-seq.fa"""
#			align_cmd = "/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmalign --outformat afa dinoSL.hmm " + cluster + "-seq.fa > " + cluster + ".aln.fa"
#			os.system(build_lib)			
			os.system(search_cmd)
			os.system(index_cmd) # make index for input file
			os.system(extr_cmd) # use table to extract sequences with hits
#			os.system(align_cmd)
hmmaln1()

