#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

#aim: make file with rep seq ID as name, then list the other IDs in there too
def splitclusters(): 
       	with open('all-trans_AA_clust-namefix-short.clstr.clstr', 'r') as fum:
       	    for line in fum:
		if '>Cluster' in line:
			new = line.replace(">", "") 
			news = new.replace(" ", "-")
			newszz = news.strip()
			clustfi = open(newszz + '_int.txt', 'w')
		else:
			clustfi.write(line.strip())
			clustfi.write("\n")

def takeoutrep():
	for file in glob('Cluster-*_int.txt'):
		naming = file.split('_')
		namings = naming[0]
        	with open(file, 'r') as elf:
			for line in elf:
#				print line
				if '*' in line:
					larp = line.split("\t")
					shoe = larp[1]
					sock = shoe.split()
					toe = sock[1]
					woot = toe[:-3]
#					print woot
					open(namings + '_' + woot + '.txt', 'w')
#need something in here to discern the rep seq.... *
#			if "*" in line:
#				l = line.split("\t")
#				clustwhole = l[1]
#				clustwholesplit = clustwhole.split()
#				clustwholesplit2 = clustwholesplit[1]
#				clustid = clustwholesplit2[:-3]
#				print clustid
#				clustfi = open(news + '_' + clustid + '.txt', 'w')
#				clustfi.write("representative" + "\t")	
#				clustfi.write(clustid.rstrip())
#				clustfi.write("\n")
#			else:
#				lop = line.split("\t")
#				wholething = lop[1]
#				partthing = wholething.split()
#				partthing2 = partthing[1]
#				idsezzz = partthing2[:-3]
#				print clustfi
##				clustfi = open(news + '_' + clustid + '.txt', 'w')
##				clustfi.write("representative" + "\t")
#				clustfiddle = open(news + '*', 'w')
#				clustfiddle.write(clustid.rstrip())
#				clustfiddle.write("\n")

#ok what if I now use the clust files in glob, split to find 
	

splitclusters()
takeoutrep()
#diffaprroach()
#extrotherseqs()
