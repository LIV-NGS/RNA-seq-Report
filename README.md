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
 ct <- counts_files[c()] 
 sm <- counts_files[c()]
```
3. Change path of directory at line 105 and 275 to full path of output report directory (C1,C2 etc. make them first if not existing) and run script for differential expression:
```
rmarkdown::render("PATH-to-the-rmd-script",output_dir = "full_path_to_output_dir")
```
