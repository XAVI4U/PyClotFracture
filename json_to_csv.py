import json
import pandas as pd
import numpy as np

filename=input("Input filename:")
#filename = 'C_25um_q'
df = pd.DataFrame()

with open(filename+'.json','r',encoding = 'utf-8') as fcc_file:
    fcc_data = json.load(fcc_file)
    df = pd.DataFrame(fcc_data['network']['segment'])
    len_total = len(df.loc["point"])
    start_point = [[0,0,0] for x in range(len_total)]
    end_point = [[0,0,0] for x in range(len_total)]
    for i in range(0,len_total):
        len_point = len(df.loc["point"][i])
        start_point[i] = df.loc["point"][i][0]
        end_point[i] = df.loc["point"][i][len_point-1]
        
    df.loc[len(df)] = start_point
    df.loc[len(df)] = end_point
    df.index = ["sid", "volume", "average_radius", "cylinder_radius", "length", "direction", "point", "radius", "start_point", "end_point"]
    
    df.to_csv(filename+'.csv', index=["sid", "volume", "average_radius", "cylinder_radius", "length", "direction", "point", "radius", "start_point", "end_point"], header=True)

print(filename)
print("Writing completed!")

fcc_file.close()