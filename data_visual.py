# Name: Yehezkiel Efraim Darmadi
# Student ID: ydar0001
# Student No: 34078215

# import libraries
import pandas as pd
import matplotlib.pyplot as plt


# import other py file for their object
from data_analyze import DataAnalyze


# create inheritance class from DataAnalyze to create a visualization
class DataVisual(DataAnalyze):
    """
    A class used to visualize graph.


    Attributes
    ----------

    Methods
    -------
    prop_val_distribution()
        create and save histogram.
    sales_trend()
        create and save a line chart
    """
    # method to create histogram
    def prop_val_distribution(self, dataframe, suburb, target_currency):
        """
        create histogram for a suburb and transformed the price.

        Returns
        ----------
        None
        """
        # local variable to store the currency list
        currency_dict = {
            "AUD": 1,
            "USD": 0.66,
            "INR": 54.25,
            "CNY": 4.72,
            "JPY": 93.87,
            "HKD": 5.12,
            "KRW": 860.92,
            "GBP": 0.51,
            "EUR": 0.60,
            "SGD": 0.88
        }

        # if the target currency is not in currency_dict.keys()
        if target_currency not in currency_dict.keys():
            # change the target_currency value into AUD and warn the user
            target_currency = "AUD"
            print("The input currency is not available, we will be substituting it with AUD")

        # get the currency exchange
        currency_exchange = currency_dict[target_currency]

        # if the suburb is all then we use the main df
        if suburb == "all":  # if the sub is not in the table then use show all
            sub_df = dataframe
        # else we filter the df by invoking the suburb_filter method
        else:
            sub_df = self.suburb_filter(dataframe, suburb)

        # invoke the currency_exchange method to change the currency
        final_arr = self.currency_exchange(sub_df, currency_exchange)

        # clean the plt
        plt.clf()
        # create a histogram
        plt.hist(final_arr, bins=50, color='blue', alpha=0.7, edgecolor = "black")
        # put title
        plt.title('Property Value Distribution' + suburb.title() + " (" + target_currency + ")")
        # put label
        plt.xlabel('Prices')
        plt.ylabel('Frequency')
        # add grid
        plt.grid(True)

        # get the file name
        file_name = "./hist_" + suburb + "_" + target_currency + ".png"
        # save the hist into the diagram folder
        plt.savefig(file_name)

        print("The histogram is successfully created.")
        print(
            "The name of the histogram: hist_" + suburb + "_" + target_currency + ".png"
        )

    # method to create line graph
    def sales_trend(self, dataframe):
        """
        create line chart to see the trend.

        Returns
        ----------
        None
        """
        # filter the df
        dataframe = dataframe[dataframe["sold_date"].notna()]
        # create a copy to get rid of the warning
        df = dataframe.copy()
        # change the format
        value = pd.to_datetime(df["sold_date"], format='%d/%m/%Y').copy()
        # replace the whole column with the new value
        df.loc[:, "sold_date"] = value

        # grouping by the df by its sold_date year
        df_group = dataframe.groupby(df["sold_date"].dt.year).size().to_frame(name="count").reset_index()

        # clean the plt
        plt.clf()
        # plot the line graph
        plt.plot(df_group["sold_date"], df_group["count"], marker = 'o')
        # create labels
        plt.xlabel("year")
        plt.ylabel("number of property sold")
        # create title
        plt.title("Trend of Number Property Sold Each Year")
        # add grid
        plt.grid(True)

        # get the file name
        file_name = "./line_sales.png"
        # save the ine graph in the diagram folder
        plt.savefig(file_name)


