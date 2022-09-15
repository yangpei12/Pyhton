import pandas as pd
import os
os.chdir("/Users/yangpei/YangPei/File/Python")
Input_data = pd.read_excel('Input/kegg背景2.xlsx', sheet_name=0)

def keggfun(id_nummber):
    Index_list = []
    for key, value in enumerate(Input_data['gene_id']):
        if value == id_nummber:
            Index_list.append(key)
        else:
            pass
    Data = Input_data.loc[Index_list, ['gene_id', 'pathway']]
    dicts = {''.join(set(Data['gene_id'])): ';'.join(list(Data['pathway']))}
    output_handle = pd.Series(dicts)
    return output_handle

for temp in Input_data['gene_id']:
    result = keggfun(temp)
    result.to_csv('Output/output_kegg背景.csv', mode='a', header=False)
