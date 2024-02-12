# RNA-seq-Report-HTML-
R markdown document to creat html reports for RNA-sequecing. 
Following are the steps to use the R markdown script.

The script used salmon quantification using gencode transcripts (download from here: https://www.gencodegenes.org/). 

After quantificaton:


1. Change directory to local directory:

counts_files <- paste0(getwd(),"/",list.dirs(recursive = FALSE,full.names = FALSE),”/quant.sf”)

2. Sort them and separate control and treated:

 ct <- counts_files[c()] 
 sm <- counts_files[c()]

3. Run script for differential expression:
