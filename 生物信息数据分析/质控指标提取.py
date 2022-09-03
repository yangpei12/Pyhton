import pandas as pd
import numpy as np
import os
import re
os.chdir('E:\scripts_input_R_python\python\Input')
Data =  pd.read_table('mRNA\mapped_stat_out.txt')

# 思路，根据输入的样本名，查找样本所在的索引，使用apply代替
def myFun(sample_name):
    Samples = Data['Sample'].tolist()
    Sample_Idx = Samples.index(sample_name)
    Sample_data = Data.iloc[Sample_Idx,:]
    return Sample_data

# 注意通常使用Series数据类型，进行apply
# 也可以使用Data.frame数据类型进行apply
result = Data['Sample'].apply(myFun)
result.to_excel('Output.xlsx')

