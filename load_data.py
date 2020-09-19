import pandas as pd


class MockData:

    def __init__(self):

        # Read relevant files
        data = pd.read_csv('data/mockdata.csv')
        description = open('data_descriptions/mock_data_description.txt', 'r')

        # Create the attributes
        self.data_all = data
        self.demographics = data[['age','age^2','sex','education']]
        self.sdmt_raw = data['sdmt_raw']
        self.bvmt_raw = data['bvmt_raw']
        self.cvlt_raw = data['cvlt_raw']
        self.columns = data.columns
        self.description = description.read()


class ConversionTable:
    def __init__(self):

        # Read relevant files
        data_sdmt = pd.read_csv('data/sdmt_conversion_table.csv')
        data_bvmt = pd.read_csv('data/bvmt_conversion_table.csv')
        data_cvlt = pd.read_csv('data/cvlt_conversion_table.csv')
        description = open('data_descriptions/conversion_table_description.txt')

        # Create the attributes
        self.sdmt = data_sdmt
        self.bvmt = data_bvmt
        self.cvlt = data_cvlt
        self.description = description.read()
