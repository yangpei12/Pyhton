import pandas as pd
path = "E:\售后\吴春霞\kog_1000.txt"
with open(path, 'r') as file_handle:
    ls = []
    for line in file_handle.readlines():
        if line.strip('\n').startswith("TRINITY"):
            new_line = line.strip('\n').split('\t')
            ls.append(new_line)

    df = pd.DataFrame(ls, columns=["query acc.ver", "subject acc.ver",
                                         "% identity", "alignment length",
                                         "mismatches", "gap opens",
                                         "q. start", "q. end", "s. start",
                                         "s. end", "evalue", "bit score"])
    df2 = df.drop_duplicates('query acc.ver')
    print(df2)