#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections, numexpr
from glob import glob
from collections import defaultdict
from re import sub

#funtion:
def findcores():
	with open('/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_.cluster_list', 'r') as listy:
#	with open('Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_.cluster_list', 'r') as listy:
#open core write file
#		cored = open('core-cluster-IDs.txt', 'w')
#open softcore write file
		softcored = open('unique-cluster-IDs.txt', 'w')
#go through cluster list
		for line in listy:
			if 'cluster' in line:
				nomclust = line.split(" ")[5] #find cluster name 
				taxxxa = line.split(" ")[3] #find taxa number
				taxnum = taxxxa.split("=")[1] #separate taxa from the 'taxa' text
#find taxa=5 print file name into core write
#				if taxnum == "5":
#					cored.write(nomclust)
#					cored.write("\n")
#find taxa=4 print file name into softcore write
				if taxnum == "1":
					softcored.write(nomclust)
					softcored.write("\n")
				else:
					continue
				
			else:
				continue

#function:
def matchcores():
#use soft-/core file to read line by line and find cluster
	with open('unique-cluster-IDs.txt', 'r') as corey:
		for ping in corey:
			pingstrip = ping.strip()
			print pingstrip
#make new file with contig ID plus _core
			thingy = open(pingstrip + '_unique.txt', 'w')
#print line ID
#			thingy.write(ping)
#			thingy.write("\n")
#use line ID to search interproscan annotations NOTE: DIFFERENT NOMENCLATURE
			with open('/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_/' + pingstrip, 'r') as clustzz:
#			with open(pingstrip, 'r') as clustzz:
				for line in clustzz:
					linestrip = line.strip()
#open cluster and read each contig ID line except australes // premature
#print annotation(s) under contig ID before next line
					if '>' in linestrip:
						thingy.write(linestrip)
						thingy.write("\n")
						if 'australes' in linestrip:
							continue
						else:
							contigwrong = linestrip.split(" ")[0]
							strainum = contigwrong.split("_")[0]
							strain = strainum.strip(">")
							species = contigwrong.split("_")[1]
							dthing = contigwrong.split("_")[2]
							cthing = contigwrong.split("_")[3]
							gthing = contigwrong.split("_")[4]
							ithing = contigwrong.split("_")[5]
							contigright = "TRINITY_" + dthing + "_" + cthing +"_" + gthing + "_" + ithing #+ "." + pthing
							with open('/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/' + strain + '_' + species + '_cluster-out.faa.gff3.GO-terms.txt', 'r') as giffy:
#							with open(strain + '_' + species + '_cluster-out.faa.gff3.GO-terms.txt', 'r') as giffy:
								colnames =  ['SEQID','SOURCE','TYPE','START','END','SCORE','STRAND','PHASE','ATTRIBUTES']
								framey = pandas.read_csv(giffy, sep='\t', names=colnames)
								pandas.set_option("display.max_colwidth",5000)
								framey = framey.set_index('SEQID')
								if contigright in framey['ATTRIBUTES']:
									attributy = framey.loc[[contigright],['ATTRIBUTES']]
									attystringy = str(attributy)		
									thingy.write(attystringy.strip())
									thingy.write("\n")
								else:
									continue

					else:
						continue

def curatecores():
	for file in glob('*_unique.txt'):
		named = file.rsplit("_", 1)[0]
		outtie = open(named + '_unique-curated.txt', 'w')
		with open(file, 'r') as innie:
			for line in innie:
				if ">" in line:
					outtie.write(line)
				elif "TRINITY" in line:
					contigtag = line.split(" ")[0]
					spacey = line.split(" ")[1:]
					putrid = [tears for tears in spacey if "GO" in tears]
					print "file: " + named
					purrid = str(putrid)
					print purrid
					twosie = purrid.split(";")[1]
					print "twosie: " + twosie
					outtie.write(twosie)
					outtie.write("\n")
				else:
					continue		

def fundicts(): #um... build a fucking dictionary for GO terms and then see what is the most common in each file, look that up
	registry = open('Unique-clusters-registry.txt', 'w')
	registry.write("file-name\tGOid;GOcount\ttotal-contigs\tcontigs-per-species")
	registry.write("\n")
	for file in glob('*_unique-curated.txt'):
		Contdict = defaultdict(int)
		name = file
		with open(file, 'r+') as what:
			GOdict = defaultdict(int) #dictionatry type makes new key with entry 0 if not present yet an entry
			for line in what:
				if ">" in line:
					strain = line.split("_")[0]
					species = line.split("_")[1]
					org = strain + "_" + species
					orca = org.strip(">")
					Contdict[orca] += 1
				else:
					splinter = line.split("\"")
					splinter.remove("Ontology_term=")
					splinter.remove("\n")
					for shrapnel in splinter:
						if "GO" in shrapnel:
							GOdict[shrapnel] += 1 #+1 to value of the corresponding key from list
			if any(GOdict) == True:
				GOwin = max(GOdict.values())
				GOid = [k for k, v in GOdict.items() if v == GOwin]
				GOwinning = str(GOwin)
				GOiding = str(GOid)	
				print "GOwinning: " + GOwinning
				print "GOiding: " + GOiding			
				what.write("GO-IDs:" + GOiding + ";number:" + GOwinning) 
			else:
				what.write("GO-IDs:None;number:0")	
				print "GO-IDs:None;number:0"
		whit = open(file, 'r')
		gosiose = str(whit.readlines()[-1])
#		print "godiose: " + gosiose
		contigose = str(sum(Contdict.values()))
		speciose = str(Contdict.items())
		registry.write(name + "\t" + gosiose + "\t" + contigose + "\t" + speciose)
		registry.write("\n")
#then polynesiensis only cluster should have poly in the file name as first species therefor move all unique w poly in name into sub folder to screen
#findcores()
#matchcores()
curatecores()
fundicts()
