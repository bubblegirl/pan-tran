#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections
from glob import glob
from collections import defaultdict
from re import sub

def kspoly(): #make one file with all the KS contig IDs
#	for file in glob('*-seq.fa'): #fasta files w all 6 ORFs of protein files
	with open('KS-poly.txt', 'w') as lemon:
		with open('CG15_Gambierdiscus-polynesiensis_hmmersearchin-seq.fa', 'r') as fasty:
#			strain = fasty.split("_")[0]
#			species = fasty.split("_")[1]
			for line in fasty:
				if ">" in line:
					contigID = line.split(" ")[0]
					dthing = contigID.split("_")[1]
					cthing = contigID.split("_")[2]
					gthing = contigID.split("_")[3]
					ithing = contigID.split("_")[4]
					contigmatch = ">CG15_Gambierdiscus-polynesiensis_" +  dthing + "_" + cthing +"_" + gthing + "_" + ithing
					lemon.write(contigmatch)
					lemon.write("\n")
					
				else:
					continue
def kscarp(): #make one file with all the KS contig IDs
#	for file in glob('*-seq.fa'): #fasta files w all 6 ORFs of protein files
	with open('KS-carp.txt', 'w') as lemon:
		with open('UTSMER9A3_Gambierdiscus-carpenteri_hmmersearchin-seq.fa', 'r') as fasty:
#			strain = fasty.split("_")[0]
#			species = fasty.split("_")[1]
			for line in fasty:
				if ">" in line:
					contigID = line.split(" ")[0]
					dthing = contigID.split("_")[1]
					cthing = contigID.split("_")[2]
					gthing = contigID.split("_")[3]
					ithing = contigID.split("_")[4]
					contigmatch = ">UTSMER9A3_Gambierdiscus-carpenteri_" +  dthing + "_" + cthing +"_" + gthing + "_" + ithing
					lemon.write(contigmatch)
					lemon.write("\n")
					
				else:
					continue
def kslap(): #make one file with all the KS contig IDs
#	for file in glob('*-seq.fa'): #fasta files w all 6 ORFs of protein files
	with open('KS-lap.txt', 'w') as lemon:
		with open('HG4_Gambierdiscus-lapillus_hmmersearchin-seq.fa', 'r') as fasty:
#			strain = fasty.split("_")[0]
#			species = fasty.split("_")[1]
			for line in fasty:
				if ">" in line:
					contigID = line.split(" ")[0]
					dthing = contigID.split("_")[1]
					cthing = contigID.split("_")[2]
					gthing = contigID.split("_")[3]
					ithing = contigID.split("_")[4]
					contigmatch = ">HG4_Gambierdiscus-lapillus_" +  dthing + "_" + cthing +"_" + gthing + "_" + ithing
					lemon.write(contigmatch)
					lemon.write("\n")
					
				else:
					continue
def kssil(): #make one file with all the KS contig IDs
#	for file in glob('*-seq.fa'): #fasta files w all 6 ORFs of protein files
	with open('KS-sil.txt', 'w') as lemon:
		with open('HG5_Gambierdiscus-silvae_hmmersearchin-seq.fa', 'r') as fasty:
#			strain = fasty.split("_")[0]
#			species = fasty.split("_")[1]
			for line in fasty:
				if ">" in line:
					contigID = line.split(" ")[0]
					dthing = contigID.split("_")[1]
					cthing = contigID.split("_")[2]
					gthing = contigID.split("_")[3]
					ithing = contigID.split("_")[4]
					contigmatch = ">HG5_Gambierdiscus-silvae_" +  dthing + "_" + cthing +"_" + gthing + "_" + ithing
					lemon.write(contigmatch)
					lemon.write("\n")
					
				else:
					continue

kspoly()
kscarp()
kslap()
kssil()
