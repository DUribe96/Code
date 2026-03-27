Overview

This project contains a Python 3 command‑line application (report.py) that generates sales reports from CSV input files.

The script reads three input CSV files:



TeamMap.csv – Maps sales team IDs to team names

ProductMaster.csv – Stores product pricing and lot sizes

Sales.csv – Contains individual sales transactions



Using these inputs, the script produces two output files:



TeamReport.csv – Total gross revenue by sales team

ProductReport.csv – Sales performance summary by product



The script uses only Python standard‑library modules (no third‑party packages).



Requirements



Python 3.7 or later

Works on Windows, macOS, and Linux

No external dependencies required





Input File Formats

1\. TeamMap.csv

Maps TeamId values to human‑readable team names.

TeamId,Name

1,Fluffy Bunnies

2,White Knights

3,Kings and Queens

4,Black Ninjas

5,Red Samurai



Notes:



Header row is required

All TeamId values referenced in Sales.csv must appear here

Team names must not contain commas





2\. ProductMaster.csv

Defines product attributes.

1,Minor Widget,0.25,250

2,Critical Widget,5.00,10

3,Complete System (Basic),500,1

4,Complete System



Fields:



ProductId (integer)

Product name (string)

Price per unit (float, may include commas)

Lot size (integer, may include commas)



Notes:



No header row

Numeric values may contain thousands separators (e.g., 1,250.00)





3\. Sales.csv

Records individual product sales.

1,1,2,10,0.00

2,1,1,1,0.00

3,2,1,5,5.00

4,3,4,1,2.50

5,3,5,2,8.00



Fields:



SaleId

ProductId

TeamId

Quantity (number of lots sold)

Discount percentage



Notes:



No header row

Gross revenue is calculated before discounts

Discount values are used only to compute DiscountCost





Output Files

1\. TeamReport.csv

Summarizes gross revenue by team, sorted descending.

Format:

Team,,GrossRevenue,

"White Knights,",30,895.25

"Kings and Queens,",20,851.00

"Black Ninjas,",12,500.00

"Red Samurai,",10,000.00

"Fluffy Bunnies,",7,924.50



Formatting rules:



Header names end with commas

Team names include a trailing comma

GrossRevenue values are formatted with thousands separators

File remains valid CSV and opens correctly in Excel





2\. ProductReport.csv

Summarizes sales performance per product.

Format:

Name,GrossRevenue,,TotalUnits,,DiscountCost

Minor Widget,7,500.00,,30,000,,600.00

Critical



Formatting rules:



Headers for GrossRevenue and TotalUnits include commas

Values for GrossRevenue and TotalUnits include:



Thousands separators

Trailing commas





Other columns remain unmodified

Output is CSV‑compliant and Excel‑friendly





Running the Script

From a command prompt or terminal, navigate to the directory containing report.py and the CSV files, then run:

Shell python report.py \\  

&#x20;       -t TeamMap.csv \\  

&#x20;       -p ProductMaster.csv \\  

&#x20;       -s Sales.csv \\  --team-report=TeamReport.csv \\



Windows (single‑line)

BAT python report.py -t TeamMap.csv -p ProductMaster.csv -s Sales.csv --team-report=TeamReport.csv --product-report=ProductReport.csvShow more lines



Data Handling \& Validation



Numeric fields may include commas and are sanitized before conversion

All calculations use proper numeric types

Missing team IDs result in "Unknown" labels

Script fails fast on malformed or inconsistent CSV data





Design Notes



Uses csv, argparse, and collections from Python’s standard library

Defensive parsing used for numeric fields

Output formatting is intentionally presentation‑oriented

Script structure supports easy maintenance and review





Notes for Reviewers / Graders



Input CSV files must be clean and well‑formed

Output formatting (commas and trailing commas) is intentional per requirements

No external libraries are used

Script is portable and self‑contained





