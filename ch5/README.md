#ALK PhD chapter 5

Work dir on HPC:
	/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis
sub-dirs:
	cores
	unique
	pks
	dinoSL
	species-gosum
	BASTAsearch

1. get-homologs

cluster_list: 
	/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_.cluster_list

cluster_directory: 
	/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_

2. KS domains
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

3. dinoSL

4. pan-transcriptome 


