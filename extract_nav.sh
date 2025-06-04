#!/bin/bash

# Download the data file from AMFI
curl -s https://www.amfiindia.com/spages/NAVAll.txt -o navdata.txt

# Extract Scheme Name and NAV (column 4 and 5)
awk -F ';' '
    NF >= 5 && $1 ~ /^[0-9]+$/ {
        scheme=$4; nav=$5;
        if (scheme != "" && nav != "")
            print scheme "\t" nav;
    }
' navdata.txt > scheme_nav.tsv

echo "Extracted data saved to scheme_nav.tsv"
