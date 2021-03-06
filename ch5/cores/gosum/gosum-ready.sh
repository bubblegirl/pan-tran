#!/bin/bash
#PBS -l ncpus=8	
#PBS -l mem=48gb
#PBS -l walltime=200:00:00
#PBS -M anna.kretzschmar@uts.edu.au
#PBS -m abe
#PBS -q c3b

module load devel/python-2.7.12

cd /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/cores/gosum

./gosum-ready.py

/shared/homes/125155/programs/GOSUM/bin/gosum Gambierdiscus-softcore-list.txt Gambierdiscus_all-species_interpro-annot.gff3 go-basic.obo 1 biological_process Gambierdiscus-softcore_gosum1-bio

/shared/homes/125155/programs/GOSUM/bin/gosum Gambierdiscus-softcore-list.txt Gambierdiscus_all-species_interpro-annot.gff3 go-basic.obo 1 molecular_function Gambierdiscus-softcore_gosum1-molec

/shared/homes/125155/programs/GOSUM/bin/gosum Gambierdiscus-softcore-list.txt Gambierdiscus_all-species_interpro-annot.gff3 go-basic.obo 1 cellular_component Gambierdiscus-softcore_gosum1-cell

/shared/homes/125155/programs/GOSUM/bin/gosum Gambierdiscus-softcore-list.txt Gambierdiscus_all-species_interpro-annot.gff3 go-basic.obo 2 biological_process Gambierdiscus-softcore_gosum2-bio

/shared/homes/125155/programs/GOSUM/bin/gosum Gambierdiscus-softcore-list.txt Gambierdiscus_all-species_interpro-annot.gff3 go-basic.obo 2 molecular_function Gambierdiscus-softcore_gosum2-molec

/shared/homes/125155/programs/GOSUM/bin/gosum Gambierdiscus-softcore-list.txt Gambierdiscus_all-species_interpro-annot.gff3 go-basic.obo 2 cellular_component Gambierdiscus-softcore_gosum2-cell
