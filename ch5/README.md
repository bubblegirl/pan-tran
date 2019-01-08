#ALK PhD chapter 5

Work dir on HPC:
	/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis
sub-dirs:
	cores
	unique
	specis-gosum 
	pks
	dinoSL

1. get-homologs

cluster_list: 
	/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_.cluster_list

cluster_directory: 
	/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_

2. pan-transcriptome
        in cores dir:
	look-for-core.py
        look-for-softcore.py
		2.1 core & softcore GO annotations
		in gosum dir:
		gosum-ready.py
		gosum-ready.sh
	in unique dir:
	look-for-unique.py
		2.2 unique GO annotations
		in gosum dir:
		gosum-ready.py
		gosum-ready.sh
	 
	
3. Species GO annotations 
	in specis-gosum dir:
	species-list-gen.py
	clean-gff3.py
	gosum-ready.sh

4. KS domains
	in pks dir:
	ks-search.py
	interpro-namefix.py
	ks-cluster-match.py
	cat KS-poly.txt >> KS-hit-list.txt
	cat KS-lap.txt >> KS-hit-list.txt
	cat KS-sil.txt >> KS-hit-list.txt
	cat KS-carp.txt >> KS-hit-list.txt
	cat KS-aust.txt >> KS-hit-list.txt
	KS-search-clusters_mark2.py
	KS-cluster-registry.py

5. dinoSL
	in dinoSL dir:
	dinoSL-search.py
