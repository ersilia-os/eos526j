# AiZynthFinder
## Model identifiers
- Slug: aizynthfinder
- Ersilia ID: 526j
- Tags: retrosynthesis, physchem, ML

# Model description
A tool for planning retrosynthesis of a target molecule. Utilizes a [pretrained model, template reactions, and reagent stock](https://figshare.com/articles/dataset/AiZynthFinder_a_fast_robust_and_flexible_open-source_software_for_retrosynthetic_planning/12334577) provided by AiZynthFinder.
- Input: SMILES
- Output: JSON file. The output json contains a hierarchical retrosynthesis path, beginning with the target molecule and including each involved reaction and reactant as a SMILES string. This output reflects the best route predicted by the aizynthfinder model. If no such route is found, an empty JSON is returned. For advanced users, please refer to the [AiZynthFinder](https://github.com/MolecularAI/aizynthfinder) repository if secondary routes or route metadata are desired. 
- Model type: Generative
- Mode of training: Pretrained

# Source code
Genheden, S., Thakkar, A., Chadimová, V. et al. AiZynthFinder: a fast, robust and flexible open-source software for retrosynthetic planning. J Cheminform 12, 70 (2020). https://doi.org/10.1186/s13321-020-00472-1
- Code: https://github.com/MolecularAI/aizynthfinder
- Checkpoints: https://figshare.com/articles/dataset/AiZynthFinder_a_fast_robust_and_flexible_open-source_software_for_retrosynthetic_planning/12334577

# License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "aizynthfinder", located at [/model](https://github.com/ersilia-os/eos526j/tree/main/model) and licensed under an [MIT license](https://github.com/ersilia-os/eos526j/blob/main/model/framework/aizynthfinder/LICENSE).

# History 
- Model was downloaded on 7/18/2022 from https://github.com/MolecularAI/aizynthfinder
- Imports were modified in scripts [aizynthfinder.py](https://github.com/ersilia-os/eos526j/blob/main/model/framework/aizynthfinder/aizynthfinder/aizynthfinder.py) and [logging.py](https://github.com/ersilia-os/eos526j/blob/main/model/framework/aizynthfinder/aizynthfinder/utils/logging.py) for eos compatibility
- Model was incorporated into the Ersilia Model Hub on 7/18/22

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
