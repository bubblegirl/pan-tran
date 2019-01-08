#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

def namefix():
	for file in glob('*cluster-out.faa'):
		strain = file.split("_")[0]
		species = file.split("_")[1]
		wrongy = open(file, 'r')
		with open(strain + '_' + species +'_' +'_hmmersearchin.faa', 'w') as slurp:
			for line in wrongy:
				if 'HG4-Gambierdiscus-lapillus' in line:
					snarf = line.replace('HG4-Gambierdiscus-lapillus_comb.1.fastq.gz-assembly.fasta', 'HG4_Gambierdiscus-lapillus')
					slurp.write(snarf.strip())
					slurp.write("\n")
				elif 'HG5-Gambierdiscus-siv' in line:
					snarf = line.replace('HG5-Gambierdiscus-sivae_comb.1.fastq.gz-assembly.fasta', 'HG5_Gambierdiscus-silvae')
					slurp.write(snarf.strip())
					slurp.write("\n")						
				else:
					slurp.write(line.strip())
					slurp.write("\n")
namefix()

