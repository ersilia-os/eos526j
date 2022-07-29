# imports
import os
import csv
import json
import sys

# hide gpus
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# point to the aizynthfinder paths
path_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "..")
sys.path.append(os.path.abspath(path_root))
sys.path.append(os.path.join(path_root, "framework", "aizynthfinder"))
from framework.aizynthfinder.aizynthfinder.aizynthfinder import AiZynthFinder

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# configure AiZynthFinder object 
root = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(root, "..", "aizynthfinder", "config.yml")
finder = AiZynthFinder(configfile=filename)
finder.stock.select("zinc")
finder.expansion_policy.select("uspto") 

# recursively cover dictionary entries to eliminate unnecessary fields
def simplify_dict(dictionary: dict, keys_to_keep: dict = ['type', 'smiles', 'children']) -> dict:
    simplified_dict = {}
    for key in dictionary.keys():
        if key in keys_to_keep:
            if type(dictionary[key]) is dict:
                simplified_dict[key] = simplify_dict(dictionary[key], keys_to_keep)
            elif type(dictionary[key]) is list:
                simplified_dict[key] = [simplify_dict(i, keys_to_keep) for i in dictionary[key]]
            else: 
                simplified_dict[key] = dictionary[key]
    return simplified_dict

def my_model(smiles_list):
    json_outputs = []
    for smi in smiles_list:

        # set target smiles and run tree search
        finder.target_smiles = smi
        finder.tree_search()
        finder.build_routes()
        stats = finder.extract_statistics()

        # process model output
        if stats['is_solved']:
            best_route = finder.routes[0]['reaction_tree'].to_dict()
            json_outputs.append(simplify_dict(best_route))
        else:
            json_outputs.append({}) # empty json object
    return json_outputs

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

# write output in a .json file
with open(output_file, "w") as f:
    json.dump(outputs, f, indent=4)



