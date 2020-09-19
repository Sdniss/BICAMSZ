 

# BICAMS regression-based norms

## Introduction - AIMS VUB

First of all, thank you very much for your interest in using our project on behalf of the Artificial Intelligence and Modelling in clinical Sciences (AIMS) lab, part of the Vrije Universiteit Brussel (VUB). We aim to contribute maximally to optimal clinical care in neurodegenerative disorders, with a special focus on Multiple Sclerosis, by performing relevant and advanced modelling on neurophysiological and brain imaging data. Moreover, in light of the prosper of the field and general understanding of our research, we do efforts to contribute to open, reproducible and transparant science by sharing code and actively practicing science communication on our [AIMS website]().

## Introduction - The project

This project is an extension to the paper of [Costers et al. 2017](https://doi.org/10.1016/j.msard.2017.08.018), which was published in Multple Sclerosis and Related Disorders. In short, the paper validated the Brief International Cognitive Assessment for Multiple Sclerosis (BICAMS) in a Belgian, Dutch-speaking population. It hereby provided regression-based norms for the 3 subtests of BICAMS:

- The Symbol Digit Modalities Test (SDMT)
- The California Verbal Learning Test, 2nd edition (CVLT-II)
- The Brief Visuospatial Memory Test Revised (BVMT-R)

The regression-based norms allow a raw score on any of the 3 cognitive tests stated above to be converted to a score that is corrected for three factors that were found in the paper to impact cognitive performance:

- Age
- Gender
- Educational status

In short, by correcting for these 3 factors, the resulting z-score can be compared to cognitive scores without interference by them. In the following section, we explain the code that performs exactly this transformation.

## Repo explanation

1. Class `Database` from mock_data.py: 
   1. `description`: if you `print` this attribute, it gives a description of the mock data that you can use to test the code.
   2. `data`: contains the actual mock data.

2. Class `Functions` from functions.py
   1. `function 1`
   2. `function 2`
   3. `function 3`



