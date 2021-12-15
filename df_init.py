import pandas as pd
import glob
import re

ann_db = pd.read_csv("database/ann_db.csv")
ann_db.rename(columns={'Unnamed: 0':'Labels'}, inplace=True)
ann_db = ann_db.set_index('Labels')
ann_db.index

# specifying the path to csv files
path = "database/signals"
# csv files in the path
files = glob.glob(path + "/*.csv")

# defining an empty list to store content
data_frame = pd.DataFrame(columns=['Fhr','UC'])
content = []

# checking all the csv files in the specified path
for filename in files:
    name = re.sub("[^0-9]", "", filename)
    df = pd.read_csv(filename, index_col=None)
    data_frame = data_frame.append(
        {
            'tag': name,
            'Fhr': df['FHR'], 
            'UC': df['UC'],
            'labels': ann_db[name]
        },
        ignore_index=True
    )
data_frame.to_csv (r'dataframe.csv', index = False, header=True)
