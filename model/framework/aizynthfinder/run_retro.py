from aizynthfinder.aizynthfinder import AiZynthFinder

filename = "config.yml"
finder = AiZynthFinder(configfile=filename)

finder.stock.select("zinc")
finder.expansion_policy.select("uspto")
# finder.filter_policy.select("uspto")

finder.target_smiles = "Cc1cccc(c1N(CC(=O)Nc2ccc(cc2)c3ncon3)C(=O)C4CCS(=O)(=O)CC4)C"
finder.tree_search()

finder.build_routes()
stats = finder.extract_statistics()

print(stats)