import pandas as pd
import os,sys,argparse
import time

def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-infile', required=True)
    parser.add_argument('-outfile', required=True)
    return parser.parse_args()

def dynamic_column(input, output):
    data_file = input
    data_file_delimiter = '\t'
    largest_column_count = 0
    with open(data_file, 'r') as temp_f:
        lines = temp_f.readlines()

        for l in lines:
            column_count = len(l.split(data_file_delimiter)) + 1
            largest_column_count = column_count if largest_column_count < column_count else largest_column_count


    temp_f.close()
    column_names = [i for i in range(0, largest_column_count)]
    df = pd.read_csv(data_file, header=None, delimiter=data_file_delimiter, names=column_names)
    df2 = df[[0, 1, 31, 40, 41, 42]]
    df2.columns = ['BindingDB-id', 'smiles', 'chemblid', 'genename', 'primary_uniprot', 'secondary_uniprot']
    df2.to_csv(output, index=None)

if __name__ == "__main__":
   args = getArgs()
   input = dynamic_column(args.infile, args.outfile)
   start = time.time()
   end = time.time()
   print('time elapsed:' + str(end - start))
