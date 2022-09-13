import pandas as pd
import os
os.chdir("E:\scripts_input_R_python\python\Input")
Input_data = pd.read_excel('kegg背景.xlsx',sheet_name=0)

for gene_id in set(Input_data['gene_id']):
    Index_list = []
    for key,value in enumerate(Input_data['gene_id']):
        if value == gene_id:
            Index_list.append(key)
    Data = Input_data.loc[Index_list,['gene_id','pathway']]
    dicts = {''.join(set(Data['gene_id'])): ';'.join(list(Data['pathway']))}
    output_handle = pd.Series(dicts)
    output_handle.to_csv('output_kegg背景.csv',mode='a', header=False)
