# pan-tran

For chapter 5 of PhD please redirtect to subdirectory `ch5`

Work flow 




In progress:
work dir: /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/

	cores

	unique

	pks

	dinoSL

	species-gosum

	BASTAsearch


cluster_list: /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_.cluster_list


cluster_directory: /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/allAA_no-clust_homologues/Gambierdiscusaustrales1_f0_0taxa_algOMCL_e0_


registry of all clusters: cluster-registry-for-venn.py


masterfile under construction: dinoSL-dict.py


KS domains:

G. lapillus 150

G. silvae 154

G. polynesiensis 221

G. carpenteri 195

G. australs 130


KS script progression:

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


BASTA:

db annot, then BASTA.. `cut -f 1 *_trembl/blast_output/*_trEMBL.out |uniq| wc -l`

-bash-4.1$ cut -f 1 carp_BASTA_trembl/blast_output/*_trEMBL.out |uniq| wc -l

169810

-bash-4.1$ cut -f 1 silvae_BASTA_trembl/blast_output/*_trEMBL.out |uniq| wc -l

126208

-bash-4.1$ cut -f 1 australes_BASTA_trembl/blast_output/*_trEMBL.out |uniq| wc -l

61161

-bash-4.1$ cut -f 1 poly_BASTA_trembl/blast_output/*_trEMBL.out |uniq| wc -l

165793


-bash-4.1$ cat CAWD149_Gambierdiscus-australes_trEMBL | wc -l

37067

-bash-4.1$ cat HG4_Gambierdiscus-lapillus_trEMBL | wc -l

71100

-bash-4.1$ cat HG5_Gambierdiscus-silvae_trEMBL | wc -l

78930

-bash-4.1$ cat CG15_Gambierdiscus-polynesiensis_trEMBL | wc -l

103053

-bash-4.1$ cat UTSMER9A3_Gambierdiscus-carpenteri_trEMBL | wc -l

106960


db-comp-dict_mark2.py for seeing what similarities and differences are between trEMBL and sp



module load bio/scripts

#need -o dir first

#swissprot

runBlast.pl -b p -f /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/CAWD149_Gambierdiscus-australes_pep-basta.fasta -n 100 -d /shared/c3/bio_db/uniprot/uniprot_sprot.fasta -o /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/australes_BASTA


#trembl

runBlast.pl -b p -f /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/CG15_Gambierdiscus-polynesiensis_pep-basta.fasta -n 250 -d /shared/c3/bio_db/uniprot/uniprot_trembl.fasta -o /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/poly_BASTA_trembl


runBlast.pl -b p -f /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/HG4_Gambierdiscus-lapillus_pep-basta.fasta -n 250 -d /shared/c3/bio_db/uniprot/uniprot_trembl.fasta -o /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/lapillus_BASTA_trembl


runBlast.pl -b p -f /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/HG5_Gambierdiscus-silvae_pep-basta.fasta -n 250 -d /shared/c3/bio_db/uniprot/uniprot_trembl.fasta -o /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/silvae_BASTA_trembl


runBlast.pl -b p -f /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/CAWD149_Gambierdiscus-australes_pep-basta.fasta -n 250 -d /shared/c3/bio_db/uniprot/uniprot_trembl.fasta -o /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/australes_BASTA_trembl


runBlast.pl -b p -f /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/UTSMER9A3_Gambierdiscus-carpenteri_pep-basta.fasta -n 250 -d /shared/c3/bio_db/uniprot/uniprot_trembl.fasta -o /shared/homes/125155/pant-transcriptomes/re-run-wo-digi/Feb18_all-AA-clust/OMCL/no-secondary-clust/cluster-analysis/BASTAsearch/carp_BASTA_trembl



/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/old-indiv-files-run/CG15_Gambierdiscus-polynesiensis_comb.1.fastq.gz-assembly.fasta_cdhit.fasta.transdecoder.pep

/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/old-indiv-files-run/HG4-Gambierdiscus-lapillus_comb.1.fastq.gz-assembly.fasta_cdhit.fasta.transdecoder.pep

/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/old-indiv-files-run/HG5-Gambierdiscus-sivae_comb.1.fastq.gz-assembly.fasta_cdhit.fasta.transdecoder.pep

/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/old-indiv-files-run/MMETSP0766_2-Gambierdiscus-australes-CAWD149.1.fastq.gz.forward_paired.fq.gz-assembly.fasta_cdhit.fasta.transdecoder.pep													

/shared/homes/125155/pant-transcriptomes/re-run-wo-digi/old-indiv-files-run/UTSMER9A3_Gambierdiscus-carpenteri_comb.1.fastq.gz-assembly.fasta_cdhit.fasta.transdecoder.pep
