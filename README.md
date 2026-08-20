# Retrosynthesis planning

Attempts to plan a synthesis for a target molecule and reports whether a route was found, how many steps it needs, how many precursors it calls for and how many of those are purchasable. AiZynthFinder, from Genheden and colleagues at AstraZeneca, searches backwards using a Monte Carlo tree search guided by reaction templates extracted from reaction databases. A solved route reflects what the template library and stock list permit, so failure indicates the search could not find a path rather than that none exists.

This model was incorporated on 2022-07-18.Last packaged on 2025-12-01.

## Information
### Identifiers
- **Ersilia Identifier:** `eos526j`
- **Slug:** `aizynthfinder`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Synthetic accessibility`, `Chemical synthesis`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `4`
- **Output Consistency:** `Fixed`
- **Interpretation:** Retrosynthesis outcome giving route score, step count, and number of precursors including those in stock.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| top_score | float | high | Score of the best solved reaction (closer to one for better solved) |
| number_of_steps | integer | low | Number of steps required for the synthesis |
| number_of_precursors | integer | low | Number of precursors required for the synthesis |
| number_of_precursors_in_stock | integer | high | Number of precursors in stock |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos526j](https://hub.docker.com/r/ersiliaos/eos526j)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos526j.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos526j.zip)

### Resource Consumption
- **Model Size (Mb):** `788`
- **Environment Size (Mb):** `1335`
- **Image Size (Mb):** `3553.99`

**Computational Performance (seconds):**
- 10 inputs: `51.59`
- 100 inputs: `1081.25`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/MolecularAI/aizynthfinder](https://github.com/MolecularAI/aizynthfinder)
- **Publication**: [https://doi.org/10.1186/s13321-020-00472-1](https://doi.org/10.1186/s13321-020-00472-1)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [svolk19-stanford ](https://github.com/svolk19-stanford )

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos526j
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos526j
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
