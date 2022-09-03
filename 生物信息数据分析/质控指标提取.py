import pandas as pd
import os
import re
os.chdir('E:\scripts_input_R_python\python\Input\mRNA')
Sample_info = pd.read_table('sample_info.txt')
#Data =  pd.read_table('mRNA\mapped_stat_out.txt')

"""
# 思路，根据输入的样本名，查找样本所在的索引，使用apply代替
def statFun(sample_name):
    Samples = Data['Sample'].tolist()
    Sample_Idx = Samples.index(sample_name)
    Sample_data = Data.iloc[Sample_Idx,:]
    return Sample_data

# 注意通常使用Series数据类型，进行apply
# 也可以使用Data.frame数据类型进行apply
result = Data['Sample'].apply(statFun)
result.to_excel('Output.xlsx')


def readFun(Arg1):
    Pattern = re.compile(r'(.+%) overall alignment rate')
    File_Path = '{0}{1}'.format(Arg1,'_bowtie_abundance_1.log')
    with open(File_Path,'r') as Input_handle:
        Lines = Input_handle.readlines()
        line = Pattern.match(Lines[5])
        Ratio = pd.Series([line.group(1)],index=[Arg1])
        return Ratio

result = Sample_info['#SampleID'].apply(readFun)
print(result)
"""


class BowtieFun:
    def __init__(self,sample):
        self.sample = sample
    def readFun(self,num):
        self.num = num
        Path = '{0}{1}{2}{3}'.format(self.sample, '_bowtie_abundance_', self.num,'.log')
        Pattern = re.compile(r'(.+%) overall alignment rate')
        with open(Path, 'r') as Input_handle:
            Lines = Input_handle.readlines()
            line = Pattern.match(Lines[5])
            Ratio = pd.Series([line.group(1)], index=[self.sample])
            return Ratio
    def mergedFun(self,bowtie1,bowtie2):
        self.bowtie1 = bowtie1
        self.bowtie2 = bowtie2
        Bowtie = pd.concat([self.bowtie1, self.bowtie2], axis=1)
        return Bowtie

bowtie1 = BowtieFun('A1').readFun(1)
bowtie2 = BowtieFun('A1').readFun(2)
Bowtie = BowtieFun('A1').mergedFun(bowtie1,bowtie2)
print(Bowtie)











