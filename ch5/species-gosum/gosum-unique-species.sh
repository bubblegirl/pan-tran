#!/bin/bash
#PBS -l ncpus=8	
#PBS -l mem=48gb
#PBS -l walltime=200:00:00
#PBS -M anna.kretzschmar@uts.edu.au
#PBS -m abe
#PBS -q c3b

module load devel/python-2.7.12


cd /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/unique/gosum/specis-diff-check

#./gosum-ready.py

#aust Aust-unique-clusters-registry.txt
/shared/homes/125155/programs/GOSUM/bin/gosum Aust-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 biological_process Aust-unique_gosum2-bio

/shared/homes/125155/programs/GOSUM/bin/gosum Aust-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 molecular_function Aust-unique_gosum2-molec

/shared/homes/125155/programs/GOSUM/bin/gosum Aust-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 cellular_component Aust-unique_gosum2-cell

/shared/homes/125155/programs/GOSUM/bin/gosum Aust-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 biological_process Aust-unique_gosum3-bio

/shared/homes/125155/programs/GOSUM/bin/gosum Aust-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 molecular_function Aust-unique_gosum3-molec

/shared/homes/125155/programs/GOSUM/bin/gosum Aust-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 cellular_component Aust-unique_gosum3-cell


#carp Carp-unique-clusters-registry.txt
#/shared/homes/125155/programs/GOSUM/bin/gosum Carp-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 biological_process Carp-unique_gosum2-bio

#/shared/homes/125155/programs/GOSUM/bin/gosum Carp-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 molecular_function Carp-unique_gosum2-molec

#/shared/homes/125155/programs/GOSUM/bin/gosum Carp-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 cellular_component Carp-unique_gosum2-cell

#/shared/homes/125155/programs/GOSUM/bin/gosum Carp-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 biological_process Carp-unique_gosum3-bio

#/shared/homes/125155/programs/GOSUM/bin/gosum Carp-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 molecular_function Carp-unique_gosum3-molec

#/shared/homes/125155/programs/GOSUM/bin/gosum Carp-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 cellular_component Carp-unique_gosum3-cell


#lap Lapillus-unique-clusters-registry.txt
#/shared/homes/125155/programs/GOSUM/bin/gosum Lapillus-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 biological_process Lapillus-unique_gosum2-bio

#/shared/homes/125155/programs/GOSUM/bin/gosum Lapillus-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 molecular_function Lapillus-unique_gosum2-molec

#/shared/homes/125155/programs/GOSUM/bin/gosum Lapillus-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 cellular_component Lapillus-unique_gosum2-cell

#/shared/homes/125155/programs/GOSUM/bin/gosum Lapillus-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 biological_process Lapillus-unique_gosum3-bio

#/shared/homes/125155/programs/GOSUM/bin/gosum Lapillus-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 molecular_function Lapillus-unique_gosum3-molec

#/shared/homes/125155/programs/GOSUM/bin/gosum Lapillus-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 cellular_component Lapillus-unique_gosum3-cell


#sil Silvae-unique-clusters-registry.txt
#/shared/homes/125155/programs/GOSUM/bin/gosum Silvae-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 biological_process Silvae-unique_gosum2-bio

#/shared/homes/125155/programs/GOSUM/bin/gosum Silvae-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 molecular_function Silvae-unique_gosum2-molec

#/shared/homes/125155/programs/GOSUM/bin/gosum Silvae-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 2 cellular_component Silvae-unique_gosum2-cell

#/shared/homes/125155/programs/GOSUM/bin/gosum Silvae-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 biological_process Silvae-unique_gosum3-bio

#/shared/homes/125155/programs/GOSUM/bin/gosum Silvae-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 molecular_function Silvae-unique_gosum3-molec

#/shared/homes/125155/programs/GOSUM/bin/gosum Silvae-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 cellular_component Silvae-unique_gosum3-cell

#/shared/homes/125155/programs/GOSUM/bin/gosum Poly-unique-clusters-registry.txt ../Gambierdiscus_all-species_interpro-annot.gff3 ../go-basic.obo 3 biological_process Poly-unique_gosum3-bio












