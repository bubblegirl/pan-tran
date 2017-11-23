#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

def readFASTAFile():
	for file in glob('*-clust.clstr'):
		fileObj = open(file, 'rU')
		sequences = []
		seq = ''
		strain = file.split("_")[0]
		ident = file.split("_")[1]
		species = strain + '_' + ident
		with open(species + '-clust.clstr.fasta', 'w') as out:
			for line in fileObj:
				if line.startswith('>'):
					if seq:
						sequences.append(seq)
					seq = ''
				else:
					seq += line.rstrip()
						
			if seq:
				sequences.append(seq)
				print >> out , sequences
#			fileObj.close()
#				out.write("\n")
#				out.write(sequences)
readFASTAFile()
			

#for file in glob('*-clust.clstr'):
#	species = file.split("_")[0]
#	strain = file.split("_")[0]
#	ident = file.split("_")[1]
#	species = strain + '_' + ident
#	with open(species + '_transdec_cd-hit_cluster-reps.fasta', 'w') as gold:
#		with open(file, 'r') as AAfile:
#			with open(species +'_cluster-reps.txt', 'r') as repids:
#				colnames = ['a']
#				df = pandas.read_csv(repids, sep='\t', names=colnames) #into dataframe with single column
#				repids = df.a.tolist()
#				for line in AAfile:
#					for ping in repids:
#						if ping in line:
#							fastaname = ping + ' [' + species + ']'
#							fastaseq = next(AAfile)
#							gold.write(fastaname.strip())
#							gold.write("\n")
#							while '>' not in next(fastaseq): #whil
#								gold.write(next(fastaseq))
#								gold.write("\n")
#							else:
#								continue
