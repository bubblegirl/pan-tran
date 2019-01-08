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

def corelist():
	corelist = open('Gambierdiscus-softcore-list.txt', 'w')
#	for file in glob("*_core-curated.txt"):
        for file in glob("/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/cores/softcore/*_softcore-curated.txt"):
		with open(file, 'r') as meep:
			for line in meep:
				if ">" in line:
					splitty = line.split(" ")[0]
					cleany = splitty.replace('>', '')
					corelist.write(cleany)
					corelist.write("\n")
				else:
					continue
#gffclean()
corelist()
