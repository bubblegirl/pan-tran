#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

def cdhit1():

def transdec(): #fix extensions
	TransDecoder.LongOrfs -t CG15_Gambierdiscus-polynesiensis_assembly_cdhit.fasta

	TransDecoder.Predict  --retain_long_orfs 100 --cpu 15 -t CG15_Gambierdiscus-polynesiensis_assembly_cdhit.fasta

def cdhit2(): #fix extensions
	for file in glob('../transdecoder/*_cdhit.fasta.transdecoder.pep'):
#	fileID = file.split(".")[0]
		with open(file, 'r'):
			cdhit_cmd = "/mnt/wonderworld/programs/cd-hit-v4.6.8-2017-0621/cd-hit-est -i " + file + " -o " + file + ".CDS-clust.clstr -T 10 -M 5000 -G 0 -c 0.98 -aS 1.00 -aL 0.005"
# -aS value varied in paper.
			os.system(cdhit_cmd)

def extrclustID(): #make doc of all rep seq IDs of clusters per organisms
	for file in glob('*-clust.clstr.clstr'):
		strain = file.split("_")[0]
		ident = file.split("_")[1]
		species = strain + '_' + ident
		with open(species + '_cluster-reps.txt', 'w') as out:
	       		with open(file, 'r') as fum:
	       		    for line in fum:
				if '>TRINITY' in line: 
					l = line.split("\t")
					clustwhole = l[1]
					clustwholesplit = clustwhole.split()
					clustwholesplit2 = clustwholesplit[1]
					clustid = clustwholesplit2[:-3]
					out.write(clustid.strip())
					out.write("\n")

def singlelineFASTA():
	for file in glob('*-clust.clstr'):
		with open(file, "r") as f:
			strain = file.split("_")[0]
			ident = file.split("_")[1]
			species = strain + '_' + ident
			with open(species + "_int-clust.fasta", "w") as output :
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
			with open(species + "_int-clust.fasta", "r") as check:
				with open(species + "_clust.fasta", "w") as gaargh:
					for line in check:
						if line.isspace():
							continue
						else:
							gaargh.write(line.strip())
							gaargh.write("\n")

def extrseq(): # rifle through transdecoder file for rep seq per cluster, extr and print
	for file in glob('*_clust.fasta'):
		strain = file.split("_")[0]
		ident = file.split("_")[1]
		species = strain + '_' + ident
		with open(species + '_transdec_cd-hit_cluster-out.faa', 'w') as gold:
			with open(file, 'r') as AAfile:
				with open(species +'_cluster-reps.txt', 'r') as repids:
					colnames = ['a']
					df = pandas.read_csv(repids, sep='\t', names=colnames) #into dataframe with single column
					repids = df.a.tolist()
					for line in AAfile:
						for ping in repids:
							if ping in line:
								fastaseq = next(AAfile)
								fastaname = ping + ' [' + species + ']'
#								print fastaname
								gold.write(fastaname.strip())
								gold.write("\n")
								gold.write(fastaseq.strip())
#								print fastaseq
								gold.write("\n")
#						gold.write(rstrip())


cdhit2()
extrclustID()
singlelineFASTA()
extrseq()		
