# Name: Yehezkiel Efraim Darmadi
# Student ID: ydar0001
# Student No: 34078215

# import libraries
import numpy as np

# import other py file for their object
from algo import Algo


# create class to analyze data
class DataAnalyze:
    """
    A class used for simply analyze data.


    Attributes
    ----------

    Methods
    -------
    currency_exchange()
        return the array of the converted pricec.
    suburb_filter()
        return filtered dataframe by a suburb.
    suburb_summary()
        return table summary of a filtered dataframe.
    avg_land_size()
        return the avg land size of a filtered dataframe.
    locate_price()
        return bool, to see whether a price is exist in a filtered dataframe.
    """
    # method to change a currency of an array
    def currency_exchange(self, dataframe, exchange_rate):
        """
        convert price using exchange_rate.

        Returns
        ----------
        array
            array which contains transformed price.
        """
        # create an array by filtering and convert it using the exchange_rate
        transformed_arr = np.array(
            # filter only the nona price data
            dataframe[dataframe["price"].notna()]["price"] * exchange_rate
        )
        # return the array
        return transformed_arr

    # method to filer df
    def suburb_filter(self, dataframe, suburb):
        """
        filtering data frame per suburb.

        Returns
        ----------
        dataframe
            filtered dataframe.
        """
        # lowering all of the subrub in the df
        sub_lower = np.array([sub.lower() for sub in dataframe["suburb"]])
        # filtering the df using the array
        sub_df = dataframe[sub_lower == suburb]
        # return the df
        return sub_df

    # method to create a summary of the df
    def suburb_summary(self, dataframe, suburb):
        """
        print the summary of a dataframe.

        Returns
        ----------
        None
        """
        # only take column bedrooms, bathrooms, and parking_spaces
        sub_df = dataframe[["bedrooms", "bathrooms", "parking_spaces"]]
        # if the suburb is not all
        if suburb != "all":
            # invoke the suburb_filer to filter the df
            sub_df = self.suburb_filter(dataframe, suburb)
            # only take column bedrooms, bathrooms, and parking_spaces
            sub_df = sub_df[["bedrooms", "bathrooms", "parking_spaces"]]

        # describe the table with 3 decimal places format
        table_result = sub_df.describe().applymap('{:,.3f}'.format)
        table_result.drop("count", inplace=True)

        # print the description
        print(table_result)
        print("----------------------\n")

    # method to calculate the avg land size
    def avg_land_size(self, dataframe, suburb):
        """
        calculate the average land size of a certain suburb.

        Returns
        ----------
        float
            the average of land size.
        """
        # filtering the df
        dataframe = dataframe[dataframe['land_size_unit'].notna()]

        # if the suburb is all then use the df else filter the df using the suburb_filter method
        if suburb == "all":
            sub_df = dataframe
        else:
            sub_df = self.suburb_filter(dataframe, suburb)

        # create an array
        arr_size = np.array(
            [
                # list comprhension, if the unit is ha then convert it to m2 else stay the same
                sub_df["land_size"].iloc[ind] * 10000
                if sub_df["land_size_unit"].iloc[ind] == "ha" else sub_df["land_size"].iloc[ind]
                for ind in range(len(sub_df["land_size"]))
            ]
        )

        # return the mean
        return arr_size.mean()

    # method to locate a price
    def locate_price(self, target_price, data, target_suburb):
        """
        locate a price in the price column per suburb.

        Returns
        ----------
        bool
            True if found.
        """
        # create algo object
        algo_method = Algo()
        # filter the df by invoking the suburb_filter method
        sub_df = self.suburb_filter(data, target_suburb)

        # filter the array
        price_arr = np.array(sub_df[sub_df["price"].notna()]["price"])

        # invoke the rev_insertion_method using the algo_method object
        price_arr = algo_method.rev_insertion(price_arr)

        # invoke the recursive_bin_search using the algo_method object
        result = algo_method.recursive_bin_search(
            list(price_arr),
            float(target_price),
            0,
            len(price_arr) - 1
        )

        # return True if the result is not equal to -1
        return result
