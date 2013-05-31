#!/bin/bash

curl "https://www.lendingclub.com/fileDownload.action?file=InFunding2StatsNew.csv&type=gen" -o data/raw/InFunding2StatsNew.csv
curl "https://www.lendingclub.com/fileDownload.action?file=LoanStatsNew.csv&type=gen" -o data/raw/LoanStatsNew.csv
curl "https://www.lendingclub.com/fileDownload.action?file=RejectStats.csv&type=gen" -o data/raw/RejectStats.csv
