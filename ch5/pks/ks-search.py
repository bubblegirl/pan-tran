#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

def hmmaln1(): #use hmmer to extract correct ORF for fastafiles and align
	for file in glob('*_hmmersearchin.faa'): #fasta files w all 6 ORFs of protein files
		species = file.split(".")[0] #get busco ID
		with open(file, 'r'):
			build_lib = "/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmbuild KS-ref-seq.hmm KS-ref-seqs.sto"
			search_cmd = "/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmsearch --tblout " + species + ".tbl KS-ref-seq.hmm " + species + ".faa"
			index_cmd = "/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/esl-sfetch --index " + species + ".faa"
			extr_cmd = "grep -v \"^#\" " + species + ".tbl | gawk \'{print $1}\' | /shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/esl-sfetch -f " + species + ".faa -> " + species + "-seq.fa"""
			align_cmd = "/shared/homes/125155/programs/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmalign --outformat afa KS-ref-seq.hmm " + species + "-seq.fa > " + species + ".aln.fa"
			os.system(build_lib)			
			os.system(search_cmd)
			os.system(index_cmd) # make index for input file
			os.system(extr_cmd) # use table to extract sequences with hits
			os.system(align_cmd)
hmmaln1()
