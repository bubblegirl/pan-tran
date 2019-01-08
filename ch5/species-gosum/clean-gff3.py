#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

#in interpro output files replace TRINITY with file species name
def gffclean():
	for file in glob("*faa.gff3"):
		strain = file.split("_")[0]
		species = file.split("_")[1]
		organsim = strain + "_" + species
		with open(file, 'r') as giffy:
			with open(organsim + "_interpro-annot.gff3", 'w') as globby:
				for line in giffy:
					if 'TRINITY' in line:
						samesy = line.replace('TRINITY', organsim)
						globby.write(samesy)
					else:
						globby.write(line)
		catty = "cat " 	+ organsim + "_interpro-annot.gff3 >> Gambierdiscus_all-species_interpro-annot.gff3"
		os.system(catty)	

gffclean()
