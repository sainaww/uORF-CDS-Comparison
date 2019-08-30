# uORF-CDS-Comparison
My study compares uORF and CDS in the two eukaryotic species, humans and zebrafish, with respect to Codon Composition and Conservation scores.

# Brief Description:

## PART I - Determining Codon Composition in upstream open reading frame (uORF) regions and coding sequences (CDS)

I extracted whole genome sequence of Danio Rerio (DR) and Homo Sapiens (HS) from UCSC:

* Danio Rerio - http://hgdownload.soe.ucsc.edu/goldenPath/danRer7/bigZips/
* Homo Sapiens - http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/
  
Using a paper as reference that had determined all the uORFs of human and Zebrafish along with CDS, I output Bed files having the uORF and CDS start and stop positions.

* https://www.ncbi.nlm.nih.gov/pubmed/26896445
  
Using these Bed files, I was able to extract these particular sequences, with the introns removed.
Traversing through the seq I counted the codons to determine the codon composition. I compared codon composition in (i) arbitrary seq of DNA that one would expect to appear by chance with uORF and (ii) uORF versus CDS. I plotted bar diagrams for visualization and found little difference in the former but noticeable difference in the latter.
I then proceeded to calculate the percentages of each type of codons being used to determine whether the usage of rare codons was higher in either of the two types of sequences. So, along with the bar diagram I output excel files for better readability of data.

## PART II - Determining Conservation Scores in uORF and CDS

I downloaded wig files containg the phyloP scores for Danio Rerio (8 way) and Homo Sapiens (100 way) and wrote a highly optimized script to traverse through the files and obtain the conservation scores of the bases in the sequences being analysed and computed their average conservation scores. I appended it to the previosly mentioned BED file. These are the links to the wiggle files.

* Danio Rerio - http://hgdownload.soe.ucsc.edu/goldenPath/danRer7/phyloP8way/
* Homo Sapiens - http://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP100way/

I then calculated the Z-scores of the means, and plotted histograms of the CDS and uORF conservation.
