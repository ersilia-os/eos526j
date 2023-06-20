# Retrosynthesis planning

A tool for planning retrosynthesis of a target molecule based on template reactions and a stock of precursors. The algorithm breaks down the input molecule into purchasable blocks until it has been completely solved.

## Identifiers

* EOS model ID: `eos526j`
* Slug: `aizynthfinder`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Generative`
* Output: `Score`
* Output Type: `String, Float`
* Output Shape: `Flexible List`
* Interpretation: The fraction of solved precursors and the number of reactions required for synthesis. Close to 1.0 for a solved compound, less than 0.8 for unsolved.

## References

* [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00472-1)
* [Source Code](https://github.com/MolecularAI/aizynthfinder)
* Ersilia contributor: [svolk19-stanford ](https://github.com/svolk19-stanford )

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos526j)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos526j.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos526j) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00472-1) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!