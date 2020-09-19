from load_data import MockData
from load_data import ConversionTable
from functions import normalization_pipeline
import pandas as pd

# Load the mock data
all_data = MockData().data_all
demographics = MockData().demographics
sdmt_raw = MockData().sdmt_raw
bvmt_raw = MockData().bvmt_raw
cvlt_raw = MockData().cvlt_raw

# Load the conversion tables
sdmt_conv_table = ConversionTable().sdmt
bvmt_conv_table = ConversionTable().bvmt
cvlt_conv_table = ConversionTable().cvlt

# Print the descriptions of the data
print(MockData().description)
print(ConversionTable().description)

# Calculate all z-scores (and binary scores (impaired / preserved)) for all tests and all subjects
z_matrix = []
tests = ['sdmt','bvmt','cvlt']
conversion_tables = [sdmt_conv_table, bvmt_conv_table, cvlt_conv_table]
raw_scores = [sdmt_raw, bvmt_raw, cvlt_raw]

for subject in range(all_data.shape[0]):

    z_row = []
    imp_row = []
    for test, conv_table, raw_score in zip(tests, conversion_tables, raw_scores):

        z_score, imp_bool = normalization_pipeline(data_vector = demographics.iloc[subject],
                                                   raw_score= raw_score.iloc[subject],
                                                   test = test,
                                                   conversion_table= conv_table,
                                                   z_cutoff= -1.5)
        z_row.append(z_score)
        imp_row.append(imp_bool)

    z_matrix.append(z_row + imp_row)

z_matrix = pd.DataFrame(data=z_matrix, columns=['sdmt_z','bvmt_z','cvlt_z',
                                                'sdmt_imp','bvmt_imp','cvlt_imp'])

#
rich_data = pd.concat([all_data, z_matrix], axis = 1)

print(rich_data)
