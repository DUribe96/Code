Overview

This project contains a Python 3 command‑line application (report.py) that generates sales reports from CSV data files.

The script reads three input CSV files:



TeamMap.csv – maps sales team IDs to team names

ProductMaster.csv – contains product details and pricing

Sales.csv – contains individual sales transactions



Using these inputs, the script produces two output CSV reports:



TeamReport.csv – total gross revenue per sales team

ProductReport.csv – sales summary per product



Only Python standard library modules are used (no third‑party packages).



Requirements



Python 3.7 or later

Operating System: Windows, macOS, or Linux

No external Python packages required





Input File Formats

1\. TeamMap.csv

Maps team IDs to team names.

Format:

TeamId,Name

1,Fluffy Bunnies

2,White Knights

3,Kings and Queens

4,Black Ninjas

5,Red Samurai



Notes:



Must include a header row

TeamId must be a positive integer

Team names must not contain commas

All TeamId values referenced in Sales.csv must appear in this file





2\. ProductMaster.csv

Contains master data for products.

Format:

1,Minor Widget,0.25,250

2,Critical Widget,5.00,10

3,Complete System (Basic),500,1

4,Complete System (Deluxe),625,1



Fields:



ProductId (integer)

Product Name (string)

Price per unit (float, may contain commas)

Lot size (integer, may contain commas)



Notes:



No header row

Numeric values may include thousands separators (e.g., 1,250.00)





3\. Sales.csv

Contains individual sales transactions.

Format:

1,1,2,10,0.00

2,1,1,1,0.00

3,2,1,5,5.00

4,3,4,1,2.50

5,3,5,2,8.00



Fields:



SaleId (integer)

ProductId (integer)

TeamId (integer)

Quantity (lots sold)

Discount percentage



Notes:



No header row

Gross revenue is calculated before applying discounts

All TeamId values listed above are mapped in TeamMap.csv





Output Files

1\. TeamReport.csv

Summarizes gross revenue by sales team.

Format:

Team,GrossRevenue

White Knights,30895.25

Kings and Queens,20851.00

Black Ninjas,12500.00

Red Samurai,10000.00

Fluffy Bunnies,7924.50



Details:



Includes a header row

Sorted by gross revenue (descending)

Gross revenue is not reduced by discounts

No team should appear as "Unknown" when input files are consistent





2\. ProductReport.csv

Summarizes sales by product.

Format:

Name,GrossRevenue,TotalUnits,DiscountCost

Critical Widget,55000.00,11000,0.00

Complete System (Deluxe),12500.00,2,312.50

Complete System (Basic),10000.00,3,650.00

Minor Widget,7500.00,30000,600.00



Details:



Includes a header row

Sorted by gross revenue (descending)

TotalUnits = Quantity × LotSize

DiscountCost reflects applied discount percentages





Running the Script



Open a command prompt or terminal

Navigate to the folder containing report.py and the CSV files

Run:



python report.py ^

&#x20; -t TeamMap.csv ^

&#x20; -p ProductMaster.csv ^

&#x20; -s Sales.csv ^

&#x20; --team-report TeamReport.csv ^

&#x20; --product-report ProductReport.csv



Data Handling and Validation



Numeric fields may include commas as thousands separators

Commas are stripped before numeric conversion

All Team IDs referenced in Sales.csv must exist in TeamMap.csv

If inconsistent data is introduced, the script will fail fast with a clear error





Design Notes



Uses only built‑in Python modules:



csv

argparse

collections





Defensive parsing is used for numeric values

No third‑party libraries (e.g., pandas)

Suitable for coursework, assessments, and lightweight reporting jobs





Author / Notes

This script is designed to be:



Readable

Maintainable

Strict about data integrity

Portable across operating systems



Correctly formatted CSV input is required for successful execution.

