#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

def transdectag(): #replace Trinity with source organism
#produce output write file to which to append the things to
	with open('all-datasets-no-reclust_AA_cdhit_transdec.fasta', 'w') as allin:#TODO fix input/output filenames
#call each pep file
		for file in glob('*.pep'):
#GET SOURCE ID
			strain = file.split("_")[0]
			organism = file.split("_")[1]
			genus = organism.split("-")[0]
			species = organism.split("-")[1]
#TODO change the nomenclature so namefix not necessary later
			source = strain + "_" + organism
			with open(file, 'r') as innit:
#read every line
				for line in innit:
#if TRINITY in line, replace with source then print to write file plus new line
					if '>' in line:
						smurf = line.split(" ")[0]
						smurfette = smurf.replace(">TRINITY", ">" + source)
						papasmurf = smurfette + ' [' + genus + ' ' + species + ']'
						allin.write(papasmurf)
						allin.write("\n")
					else:
						allin.write(line)
						allin.write("\n")


def singlelineFASTA():#TODO fix input/output file names
	with open('all-datasets-no-reclust_AA_cdhit_transdec.fasta', 'r') as f:
#		with open(file, "r") as f:
#			strain = file.split("_")[0]
#			ident = file.split("_")[1]
#			species = strain + '_' + ident
		with open('allAA_int-noclust.fasta', 'w') as output :
			seq =""
			for line in f :
				if line.startswith(">"):
					if seq != "":
						output.write(seq)
						seq=""
					seq += "\n"+line     
				else:
					seq += line.strip().replace("\n", '')
			else:
				if seq != "":
					output.write(seq)
					seq=""
		with open("allAA_int-noclust.fasta", "r") as check:
			with open("allAA_no-clust.fasta", "w") as gaargh:
				for line in check:
					if line.isspace():
						continue
					else:
						gaargh.write(line.strip())
						gaargh.write("\n")

transdectag()
singlelineFASTA()
