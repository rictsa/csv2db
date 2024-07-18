import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@localhost:5432/myDB",
                       connect_args={'options': '-csearch_path={}'.format("my_schema")})

# generate dtype based on quotes
f = open("myfile.csv", "r", encoding="utf-8")
lines = f.readlines()
header = lines[0]
sample = lines[1]
dtype_dict = {}

# loop through header and add type based on quotes in sample
headerlist = header.split(',')
ind = 0
for head in headerlist:
    holder = ''
    samplelist = sample.split(',')
    
    if '"' not in samplelist[ind]:
        dtype_dict[head.strip('"')]='Int64'
    elif samplelist[ind].startswith('"') and samplelist[ind].endswith('"'):
        dtype_dict[head.strip('"')]='object'
    elif samplelist[ind].startswith('"'):
        for lookup in range(ind+1, len(samplelist)):
            if samplelist[lookup].endswith('"'):
                ind = lookup
                dtype_dict[head.strip('"')]='object'
                break
    ind += 1
            
dtype_dict['FlightDate']='object'

df = pd.read_csv("myfile.csv", header=0,index_col=False,quotechar='"',
                 doublequote=False,engine='python',dtype=dtype_dict)

df.to_sql("flight", con=engine, index=False) #, if_exists='append'
