# csv2db
for some CSV files, strings are quoted with double quotes, and sometimes there would be commas within the double-quoted column
pandas' to_sql function can't properly handle those columns, I encountered mistyped columns in the resulting database table
this python tool is to import the CSV file into PostgreSQL properly, with desired table column types

steps:
read csv file, first row is header and use second row as the sample to decide the data type
find all double quotes in pairs, see the quoted string as a whole, use a dictionary to record the data type for each column
import into postgresql using the dictionary created from above step
