#!/usr/bin/python3

"""Pipeline for RNA seq quantification

Usage:
 rna-seq.py quant-pe REF [-t <x>]
 rna-seq.py quant-se REF [-t <x>]
 rna-seq.py (-h | --help)


Options:
  -h --help                 Show this screen.
   REF                      Full path to salmon index.
  -t --threads=<x>          Number of threads to use for alignment [default: 4].

"""
import docopt
import os
from subprocess import *


def rna1(ref_index,th):
    fastq = [fq for fq in os.listdir('.') if "R1" in fq]

    for f in fastq:
        Popen(
            "salmon quant -p %d -i %s -l A -1 %s -2 %s -o transcripts_quant_%s --seqBias --posBias --validateMappings" % (th,ref_index,f,
            f.replace("_R1_001.fastq.gz", "_R2_001.fastq.gz"), f.replace("_R1_001.fastq.gz", "")), shell=True)


def rna2(ref_index,th):
    fastq = [fq for fq in os.listdir('.') if ".fastq.gz" in fq]

    for f in fastq:
        Popen(
            "salmon quant -p %d -i %s -l A -r %s -o transcripts_quant_%s --seqBias --posBias --fldMean 350 --validateMappings" % (th,ref_index,
            f, f.replace(".fastq.gz", "")), shell=True)


#####################################
#############    MAIN   #############
#####################################


if __name__ == '__main__':
    try:
        args = docopt.docopt(__doc__, version='rna-seq-v1.0')

        if args['quant-pe']:
            rna1(args['REF'],args['--threads'])

        elif args['quant-se']:
            rna2(args['REF'],args['--threads'])

    except docopt.DocoptExit:
        print("Operation Failed (Check Arguments) !! for help use: python chrom-seq.py -h or --help")
