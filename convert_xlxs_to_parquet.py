import os
import fnmatch
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

path = './'
pattern = '*.xlsx'
all_files = os.listdir(path)

for name in all_files:
    if fnmatch.fnmatch(name, pattern):
        df = pd.read_excel(name)
        table = pa.Table.from_pandas(df)
        pq.write_table(table, name + '.parquet')
