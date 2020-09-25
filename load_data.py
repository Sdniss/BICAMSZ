import pandas as pd


class InputData:

    def __init__(self):

        # Read relevant files
        data = pd.read_excel('data/data_to_transform.xlsx')
        description = open('data_descriptions/data_to_transform_description.txt', 'r')

        # region Perform checks if the data was correctly entered

        error_dict = {'columns': 'Please be sure to use the correct column names and that they are lower case',
                      'age': 'Please use age values between 0 and 125 years',
                      'sex': 'Please assure the following encoding: Male = 1, Female = 2',
                      'education': 'Please use education levels that are encoded as 6, 12, 13, 15, 17 or 21 years',
                      'sdmt': 'Please use sdmt values between 0 and 110',
                      'bvmt': 'Please use bvmt values between 0 and 36',
                      'cvlt': 'Please use cvlt values between 0 and 80'}

        allowed_range_dict = {'columns': {'age', 'sex', 'education', 'sdmt', 'bvmt', 'cvlt'},
                              'age': set(range(0,126)),
                              'sex': {1,2},
                              'education': {6,12,13,15,17,21},
                              'sdmt': set(range(0,111)),
                              'bvmt': set(range(0,36)),
                              'cvlt': set(range(0,80))}

        for key in error_dict.keys():
            # Extract the data vector for a specific key
            if key == 'columns':
                input_vector = set(data.columns)
            else:
                input_vector = set(data[key])
            # Check whether the vector is within the allowed range
            if not input_vector.issubset(allowed_range_dict.get(key)):
                raise ValueError(error_dict.get(key))

        # endregion

        # add age^2 column as second column to the data
        age_2 = data['age']**2
        data.insert(loc=1, column='age^2', value=age_2)  # insert age^2 column in second position (thus loc = 1)

        # Create the attributes
        self.data_all = data
        self.demographics = data[['age','age^2','sex','education']]
        self.cognitive = data.drop(['age','age^2','sex','education'], axis=1)
        self.columns = data.columns
        self.description = description.read()

        
class ConversionTable:
    def __init__(self):

        # Read relevant files
        data_sdmt = pd.read_csv('data/conversion_tables/sdmt_conversion_table.csv')
        data_bvmt = pd.read_csv('data/conversion_tables/bvmt_conversion_table.csv')
        data_cvlt = pd.read_csv('data/conversion_tables/cvlt_conversion_table.csv')
        description = open('data_descriptions/conversion_table_description.txt')

        # Create the attributes
        self.sdmt = data_sdmt
        self.bvmt = data_bvmt
        self.cvlt = data_cvlt
        self.description = description.read()
