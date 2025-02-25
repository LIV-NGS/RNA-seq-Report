# RNA-seq-Report
R markdown document to creat html reports for RNA-sequecing. 
Following are the steps to use the R markdown script.

The script used salmon quantification using gencode transcripts (download from here: https://www.gencodegenes.org/). 
Download salmon: https://salmon.readthedocs.io/en/latest/

After quantificaton:


1. Change directory to local directory:
```
counts_files <- paste0(getwd(),"/",list.dirs(recursive = FALSE,full.names = FALSE),"/quant.sf")
```

3. Sort them and separate control and treated:
```
Depending on the number of replicates,

ct <- counts_files[c(...)]
Example1:
ct <- counts_files[c(1:3)]
sm <- counts_files[c(4:6)]

Example2:
ct <- counts_files[c(1,4,5)]
sm <- counts_files[c(2,3,6)]

```
3. Change path of directory at .... to full path of output report directory (C1,C2 etc. make them first if not existing) and run script for differential expression:
```
rmarkdown::render("PATH-to-the-rmd-script",output_dir = "full_path_to_output_dir")
```
