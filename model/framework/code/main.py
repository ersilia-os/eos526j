# imports
import os
import csv
import sys
import pandas as pd
import numpy as np

from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from framework.aizynthfinder.aizynthfinder.aizynthfinder import AiZynthFinder


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]


cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")

# configure AiZynthFinder object 
filename = "aizynthfinder/config.yml"
finder = AiZynthFinder(configfile=filename)
finder.stock.select("zinc")
finder.expansion_policy.select("uspto")
os.chdir(cwd)
    

def my_model(smiles_list):
    output_df = pd.DataFrame(columns=["Synthesis Score"])
    for smi in smiles_list:

        # set target smiles and run tree search
        finder.target_smiles = smi
        finder.tree_search()
        finder.build_routes()
        stats = finder.extract_statistics()

        # process model output
        if stats['is_solved']:
            output_df.loc[len(output_df.index)] = [stats['top_score']]
        else:
            output_df.loc[len(output_df.index)] = [np.NaN]

    return output_df

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

# write outputs to file (outputs is a pd dataframe)
outputs.to_csv(output_file, index=False)
