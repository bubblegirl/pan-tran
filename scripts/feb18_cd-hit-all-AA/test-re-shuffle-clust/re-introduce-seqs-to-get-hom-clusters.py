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

def repname():
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
					datone = open(namings + '_' + woot + '.txt', 'w')
				else:
 					continue
#whaaaat if I glob the write file and then extract the cluster name from there? all followed bu int so that should be doable
def takeoutrep():
	for file in glob('Cluster-*>*.txt'):
		naming = file.split('_')
		namings = naming[0]
		with open(file, 'w') as yaarp:
			with open(namings + '_int.txt', 'r') as snarfle:
				for line in snarfle:
					if '*' in line:
						continue
					else:
						nosey = line.split("\t")
						wosey = nosey[1]
						whisker = wosey.split()
						twitch = whisker[1]
						wiggle = twitch[:-3]
						yaarp.write(wiggle.strip())
						yaarp.write("\n")
#next need to go through each cluster file
def lookupAA():
	for file in glob('Cluster-*>*.txt'):
		with open(file, 'r+') as flower:
			with open('allAA_clust-namefix.fasta', 'r') as field:
				for line in flower:
					petal = line
					for line in field:
						blade = line
						print petal
						print blade
#incompatibility in na,ing convention between the files
						if petal in blade:
							print petal					
#			with open('all-trans_AA_clust-namefix.clstr', 'r') as field:
#				leaf = line in field
					

#			for line in elf:
#				print line
#				with open(datone, 'w') as yesssz:
#					if '*' in line:
#						continue
#					else:
#						plz = line.split("\t")
#						works = plz[1]
#						wif = works.split()
#						stoopid = wif[1]
#						nestings = stoopid[:-3]
#						print nestings				
				#how the fuck do I open the next write file with the actual ID? Ideally I'd read from elf, then print any line wihtout a wild card in it into the new file which has the the cluster and rep ID in the name.
#	for file in glob('Cluster-*_int.txt'):
#		nam = file.split('_')
#		nams = nam[0]
#		with open(nams + "_>*.txt", 'r') as cerne:
#			print cerne
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
repname()
takeoutrep()
lookupAA()
#diffaprroach()
#extrotherseqs()
