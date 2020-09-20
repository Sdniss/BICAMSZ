from load_data import InputData
from load_data import ConversionTable
from functions import normalization_pipeline
import pandas as pd

# region Load data
# Load the mock data
input_data = InputData().data_all
demographics = InputData().demographics
cognitive_raw = InputData().cognitive

# Load the conversion tables
sdmt_conv_table = ConversionTable().sdmt
bvmt_conv_table = ConversionTable().bvmt
cvlt_conv_table = ConversionTable().cvlt
conversion_table_dict = {'sdmt': sdmt_conv_table,
                         'bvmt': bvmt_conv_table,
                         'cvlt':cvlt_conv_table}
# endregion

# region Calculate all z-scores and binary scores (impaired / preserved) for all tests and all subjects
# General initiations
z_cutoff = -1.5
transform_matrix = []

for subject in range(input_data.shape[0]):

    # Initiations per subject
    z_row = []
    imp_row = []

    for test_column in cognitive_raw.columns:

        # Extract raw data from dataframe
        raw_scores = cognitive_raw[test_column]

        # Get the test, which are the first 4 digits of the column name, (sdmt, bvmt or cvlt)
        test = test_column[0:4]

        # Get correct conversion table
        conv_table = conversion_table_dict.get(test)

        # Calculate z-score and whether it is impaired or not for the test and subject
        z_score, imp_bool = normalization_pipeline(data_vector = demographics.iloc[subject],
                                                   raw_score= raw_scores.iloc[subject],
                                                   test = test,
                                                   conversion_table= conv_table,
                                                   z_cutoff= z_cutoff)
        # Append lists
        z_row.append(z_score)
        imp_row.append(imp_bool)

    # Append to general matrix
    transform_matrix.append(z_row + imp_row)

# endregion

# region Put in matrix
# Define new columnnames for dataframe
z_score_columns = [element.replace('_raw', '') + '_z' for element in cognitive_raw.columns]
imp_columns = [element.replace('_raw', '') + '_imp' for element in cognitive_raw.columns]
new_columns = z_score_columns + imp_columns

# Convert matrix to pandas dataframe
transform_matrix = pd.DataFrame(data=transform_matrix,
                                columns=new_columns)
# endregion

# Concatenate original data with the z-scores and impairment boolean columns
transformed_data = pd.concat([input_data, transform_matrix], axis = 1)

# Save the richto data folder
transformed_data.to_csv('data/transformed_data.csv', index=False)

print(transformed_data)
