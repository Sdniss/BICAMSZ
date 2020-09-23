# BICAMS z-normalization

## Introduction - AIMS VUB

First of all, thank you very much for your interest in using our project on behalf of the Artificial Intelligence and Modelling in clinical Sciences (AIMS) lab, part of the Vrije Universiteit Brussel (VUB). We aim to contribute maximally to optimal clinical care in neurodegenerative disorders, with a special focus on Multiple Sclerosis, by performing relevant and advanced modelling on neurophysiological and brain imaging data. Moreover, in light of the prosper of the field and general understanding of our research, we do efforts to contribute to open, reproducible and transparant science by sharing code and actively practicing science communication on our [AIMS website]().

## Introduction - The project

This project is an extension to the paper of [Costers et al. 2017](https://doi.org/10.1016/j.msard.2017.08.018), which was published in Multple Sclerosis and Related Disorders. In short, the paper validated the Brief International Cognitive Assessment for Multiple Sclerosis (BICAMS) in a Belgian, Dutch-speaking population. It hereby provided regression-based norms for the 3 subtests of BICAMS:

- The Symbol Digit Modalities Test (SDMT)
- The California Verbal Learning Test, 2nd edition (CVLT-II)
- The Brief Visuospatial Memory Test Revised (BVMT-R)

The regression-based norms allow a raw score on any of the 3 cognitive tests stated above to be converted to a score that is corrected for three factors that were found in the paper to impact cognitive performance:

- Age
- Age^2
- Gender
- Educational status

In short, by correcting for these 4 factors, the resulting z-score can be compared to cognitive scores without interference by them. In the "Repo explanation" section, we explain the code that performs exactly this transformation.

## Deliverables

With this code, you can easily transform cognitive scores on BICAMS to z-scores by following the steps listed in "How to run it + dependencies". A dataframe will be returned that you can subsequently use for your projects.

## Repo explanation

The project adopts the following file structure:

1. `BICAMS_application.py`: the main script that performs the transformation. It depends on the following elements:

   1. Data (`load_data.py`). Location of the data and description in the "data" and "data_descriptions" folder respectively.

      - class `InputData`: the input data to be transformed

        Attributes:

        - `data_all`: all input data
        - `demographics`: subset of input data, 'age', 'gender', 'education' columns
        - `sdmt`: subset of input data, 'sdmt' column
        - `bvmt`: subset of input data, 'bvmt' column
        - `cvlt`: subset of input data, 'cvlt' column
        - `columns`: columnnames of the input data
        - `description`: description of the data
        
- class `ConversionTable`: a look-up table that is used for the conversion from raw to scaled scores
      
  Attributes:
      
  - `sdmt`: sdmt conversion table
  - `bvmt`: bvmt conversion table
  - `cvlt`: cvlt conversion table
  - `description`: description of the structure of a conversion table
    
2. Functions (`functions.py`)
   
   - `normalization_pipeline` is the mother function that combines all other functions to do the normalization:
      - `get_expected_score` generates an expected cognitive score
      - `raw_to_scaled` converts raw value to scaled value
      - `to_z_score` turns the expected and scaled score to a z-score
      - `impaired_or_not` declares whether the z-score is impaired or not

## Set up the environment + run the main script

General: Make sure to have any version of python 3 installed on your computer

### Clone the repository to your local computer

Please open a terminal window in a folder that will subsequently contain the GitHub repo after running following command: `git clone https://github.com/Sdniss/BICAMS_normalization`. Subsequently, type `cd BICAMS_normalization` to enter that folder in the terminal.

### Environment set-up: 

To be able to run the eventual script, we first have to set up the environment containing the correct dependencies that the code relies on. By running `python setup_environment.py`, a virtual environment called `BICAMS_app_venv` is created within your local repository and subsequently enriched with the dependencies that are listed in `dependencies.txt`.

### Preparation and running the main script

To perform the calculations for z-scores and impairment per domain, complete the following steps:

1. Prepare your dataframe to meet the following requirements:

   - Filename: `data_to_transform.csv`

   - Column headers: `age`, `sex`, `ecucation`, `sdmt`, `bvmt`, `cvlt`

     Note 1: please use exactly these column names in this order

     Note 2: only the 3 first columns are an absolute requirement. For the cognitive scores, please prepare your dataframe to only contain columns for which you have data. Hence, this can be a subset of the latter 3 columns, but should at least include one of them

2. Upload your file to the `data` directory. It will replace the `data_to_transform.csv` that is currently there, and which is just mock data included by default

3. Run either the `BICAMS_script.py` file or the `BICAMS_script.ipynb` file if you are a jupyter notebook user

4. Extract the transformed data from the data folder: `transformed_data.csv`. Also checkout the description of what the output, `transformed_data.csv`, contains. It is located within the `data_descriptions folder`, and is called `transformed_data_description.txt`

