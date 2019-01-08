#!/usr/bin/env python
import os, sys, glob, pandas, re, shutil, collections, numexpr
from glob import glob
from collections import defaultdict
from re import sub

for file in glob('*.pep'):
	strain = file.split("_")[0]
	species = file.split("_")[1]
	organism = strain + "_" + species
	listed = open(organism + '-list.txt', 'w')
	with open(file, 'r') as intro:
		for line in intro:
			if ">" in line:
				ID = line.split(" ")[0]
				dthing = ID.split("_")[1]
				cthing = ID.split("_")[2]
				gthing = ID.split("_")[3]
				ipthing = ID.split("_")[4]
				worm = organism + "_" + str(dthing) + "_" + str(cthing) + "_" + str(gthing) + "_" + str(ipthing)
				listed.write(worm)
				listed.write("\n")
			else:
				continue
