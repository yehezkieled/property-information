# Name: Yehezkiel Efraim Darmadi
# Student ID: ydar0001
# Student No: 34078215

# import libraries
import pandas as pd


# create class data to extract data from the csv file
class Data:
    """
    A class used to extract data from the csv file


    Attributes
    ----------

    Methods
    -------
    extract_property_info()
        return the dataframe from the csv file
    """
    # extract the csv file
    def extract_property_info(self, path):
        """
        generate dataframe from the csv file

        Returns
        ----------
        dataframe
            dataframe from the csv file
        """
        property_info_df = pd.read_csv(path)
        return property_info_df
