#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

def transdectag(): #replace Trinity with source organism
#produce output write file to which to append the things to
	#with open('all-datasets-no-reclust_AA_cdhit_transdec.fasta', 'w') as allin:#TODO fix input/output filenames
#call each pep file
	for file in glob('*.fasta'):
#GET SOURCE ID
		strain = file.split("_")[0]
		organism = file.split("_")[1]
		genus = organism.split("-")[0]
		species = organism.split("-")[1]
#TODO change the nomenclature so namefix not necessary later
		source = strain + "_" + organism
		with open(source + '_supertrans.fasta', 'w') as sup:
			with open(file, 'r') as innit:
#read every line
				for line in innit:
#if TRINITY in line, replace with source then print to write file plus new line
					if '>' in line:
#						smurf = line.split(" ")[0]
						smurfette = line.replace(">TRINITY", ">" + source)
#						papasmurf = smurfette + ' [' + genus + ' ' + species + ']'
						sup.write(smurfette)
	#					sup.write("\n")
					else:
						sup.write(line)
	#					sup.write("\n")

transdectag()
