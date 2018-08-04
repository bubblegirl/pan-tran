#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections, numexpr
from glob import glob
from collections import defaultdict
from re import sub

#funtion:
def findcores():
#	with open('/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_.cluster_list', 'r') as listy:
	with open('Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_.cluster_list', 'r') as listy:
#open core write file
		cored = open('core-cluster-IDs.txt', 'w')
#open softcore write file
		softcored = open('softcore-cluster-IDs.txt', 'w')
#go through cluster list
		for line in listy:
			if 'cluster' in line:
				nomclust = line.split(" ")[5] #find cluster name 
				taxxxa = line.split(" ")[3] #find taxa number
				taxnum = taxxxa.split("=")[1] #separate taxa from the 'taxa' text
#find taxa=5 print file name into core write
				if taxnum == "5":
					cored.write(nomclust)
					cored.write("\n")
#find taxa=4 print file name into softcore write
				if taxnum == "4":
					softcored.write(nomclust)
					softcored.write("\n")
				else:
					continue
				
			else:
				continue

#function:
def matchcores():
#use soft-/core file to read line by line and find cluster
	with open('core-cluster-IDs.txt', 'r') as corey:
		for ping in corey:
			pingstrip = ping.strip()
#make new file with contig ID plus _core
			thingy = open(pingstrip + '_core.txt', 'w')
#print line ID
#			thingy.write(ping)
#			thingy.write("\n")
#use line ID to search interproscan annotations NOTE: DIFFERENT NOMENCLATURE
#			with open('/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_/' + ping, 'r') as clustzz:
			with open(pingstrip, 'r') as clustzz:
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
#							pthing = contigwrong.split(".")[1]
							contigright = "TRINITY_" + dthing + "_" + cthing +"_" + gthing + "_" + ithing #+ "." + pthing
#							with open('/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/' + strain + '_' + species + '_cluster-out.faa.gff3.GO-terms.txt', 'r') as giffy:
							with open(strain + '_' + species + '_cluster-out.faa.gff3.GO-terms.txt', 'r') as giffy:
								colnames =  ['seqid','source','type','start','end','score','strand','phase','attributes']
								framey = pandas.read_csv(giffy, sep='\t', names=colnames)
								framey = framey.set_index('seqid')
								attributy = framey.loc[[contigright],['attributes']]
								attystringy = str(attributy)
								print attystringy
								print type(attystringy)								
#								thingy.write(attributy)
#								thingy.write("\n")
#								atriboot = attributy.to_string()
#								goey = atriboot.split(";")[2]
#								goey = attributy.split(";")[2]
#								print isinstance(atriboot, str)
#framey.query('seqid == @contigright')['attributes'] #error brcause @contig designation is a df feature, not a pandas one
#								atriboot = attributy.to_string()
#								goey = atriboot.split(";")[2]
#								thingy.write(goey)
#								thingy.write("\n")
					else:
						continue

				



#findcores()
matchcores()
