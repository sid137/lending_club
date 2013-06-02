#!/usr/bin/env Rscript

library(rbundler)
bundle(.)

download.file( "https://www.lendingclub.com/fileDownload.action?file=LoanStatsNew.csv&type=gen", 'data/loan_stats.csv')
