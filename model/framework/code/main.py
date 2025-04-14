# imports
import os
import csv
import json
import sys

# hide gpus
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# point to the aizynthfinder paths
root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(root))
sys.path.append(os.path.join(root, "..", "framework", "aizynthfinder"))
from aizynthfinder.aizynthfinder import AiZynthFinder

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")

# configure AiZynthFinder object 
filename = os.path.join(root, "config.yml")
finder = AiZynthFinder(configfile=filename)
finder.stock.select("zinc")
finder.expansion_policy.select("uspto")
os.chdir(cwd)  

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
    results = []
    for smi in smiles_list:
        # set target smiles and run tree search
        finder.target_smiles = smi
        finder.tree_search()
        finder.build_routes()
        stats = finder.extract_statistics()
        print(stats)

        # Keep reaction steps
        if stats['is_solved']:
            best_route = finder.routes[0]['reaction_tree'].to_dict()
            json_outputs.append(simplify_dict(best_route))
        else:
            json_outputs.append({}) # empty json object
        
        # Keep stock information
        if stats['is_solved']:
            results.append({
                "top_score": stats["top_score"],
                "number_of_steps": stats["number_of_steps"],
                "number_of_precursors": stats["number_of_precursors"],
                "number_of_precursors_in_stock": stats["number_of_precursors_in_stock"]
            })
    return results,json_outputs

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]

# run model
results,_ = my_model(smiles_list)

keys = results[0].keys()  # Get headers from first item

with open(output_file, "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(results)



