# Convert Excel XLSX files to Parquet

Run this program in the current directory and it will (try to) convert each .xlsx file to a new parquet file - with the same filename with a ".parquet" extension.

Although this does work for simple .xlsx files, there are still various data-dependent issues that can make conversion fail.

### Run the program: 
It does not currently have a #! line, to select the interpreter. Use a command like this to run it:   

```shell
python3 convert_xlsx_to_parquet
``` 
