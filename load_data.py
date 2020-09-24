import pandas as pd


class InputData:

    def __init__(self):

        # Read relevant files
        data = pd.read_excel('data/data_to_transform.xlsx')
        description = open('data_descriptions/data_to_transform_description.txt', 'r')

        # region Perform checks if the data was correctly entered
        # column names
        if not set(data.columns).issubset({'age', 'sex', 'education', 'sdmt', 'bvmt', 'cvlt'}):
            raise ValueError('Please be sure to use the correct column names and that they are lower case')
        # sex
        if data['sex'].unique().sum() != 3:  # Assure that 1's and 2's were passed for male and female respectively
            raise ValueError('Please assure the following encoding: Male = 1, Female = 2')
        # education
        if not set(data['education']).issubset({6, 12, 13, 15, 17, 21}):
            raise ValueError('Please use education levels that are encoded as 6, 12, 13, 15, 17 or 21 years')
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
