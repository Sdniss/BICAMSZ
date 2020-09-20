from load_data import InputData
from load_data import ConversionTable
from functions import normalization_pipeline
import pandas as pd

# region Load data
# Load the mock data
input_data = InputData().data_all
demographics = InputData().demographics
sdmt_raw = InputData().sdmt_raw
bvmt_raw = InputData().bvmt_raw
cvlt_raw = InputData().cvlt_raw

# Load the conversion tables
sdmt_conv_table = ConversionTable().sdmt
bvmt_conv_table = ConversionTable().bvmt
cvlt_conv_table = ConversionTable().cvlt
# endregion

# region Calculate all z-scores and binary scores (impaired / preserved) for all tests and all subjects
# Initiations
transform_matrix = []
tests = ['sdmt','bvmt','cvlt']
conversion_tables = [sdmt_conv_table, bvmt_conv_table, cvlt_conv_table]
raw_scores = [sdmt_raw, bvmt_raw, cvlt_raw]
for subject in range(input_data.shape[0]):

    # Initiations per subject
    z_row = []
    imp_row = []
    for test, conv_table, raw_score in zip(tests, conversion_tables, raw_scores):

        # Calculate z-score and whether it is impaired or not for the test and subject
        z_score, imp_bool = normalization_pipeline(data_vector = demographics.iloc[subject],
                                                   raw_score= raw_score.iloc[subject],
                                                   test = test,
                                                   conversion_table= conv_table,
                                                   z_cutoff= -1.5)
        # Append lists
        z_row.append(z_score)
        imp_row.append(imp_bool)

    # Append to general matrix
    transform_matrix.append(z_row + imp_row)

# Convert matrix to pandas dataframe
transform_matrix = pd.DataFrame(data=transform_matrix,
                                columns=['sdmt_z','bvmt_z','cvlt_z','sdmt_imp','bvmt_imp','cvlt_imp'])

# endregion

# Concatenate original data with the z-scores and impairment boolean columns
transformed_data = pd.concat([input_data, transform_matrix], axis = 1)

# Save the richto data folder
transformed_data.to_csv('data/transformed_data.csv', index=False)
