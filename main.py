# Name: Yehezkiel Efraim Darmadi
# Student ID: ydar0001
# Student No: 34078215

# import other .py file
from main_menu import MainMenu
from data import Data
from data_visual import DataVisual

# import libraries
import os


# function to run the app
def main():
    """
    run the whole system application

    Returns
    ----------
    none
    """
    # check whether the data exist or not
    data_dir = "./property_information.csv"

    # checking whether the data folder exists
    if not os.path.exists("./" + data_dir):
        # if not, tell the user to put the correct csv file
        print("Please input the correct csv file and rerun the app.")
        return

    # options available in the app
    options = [
        "1. List of suburb",
        "2. Summary of Properties",
        "3. Average Land Size (m²)",
        "4. Property Value Distribution",
        "5. Sales Trend",
        "6. Locate Price",
        "7. Exit"
    ]

    # create main menu object
    m_menu = MainMenu(options)

    # create a data object
    data_obj = Data()

    # extract the csv file to get df
    main_df = data_obj.extract_property_info(data_dir)

    # getting the suburb list
    suburb_list_unique = main_df["suburb"].unique()
    # use lower method for all of the elements
    suburb_list_unique = [sub.lower() for sub in suburb_list_unique]

    # create analyze object
    analyze_obj = DataVisual()
    # currency info
    currency_info_list = [
        "AUD: Australian Dollar",
        "USD: United States Dollar",
        "INR: Indian Rupee",
        "CNY: Chinese Yuan",
        "JPY: Japanese Yen",
        "HKD: Hong Kong Dollar",
        "KRW: Korean Won",
        "GBP: Great Britain Poundsterling",
        "EUR: Euro",
        "SGD: Singaporean Dollar"
    ]

    # while true, keep on running
    while True:
        # print the main menu
        print(m_menu)

        # user input initiate to make the yellow line disappear
        user_input_main = 0
        # while true keep on asking the user to give correct input
        while True:
            # try error
            try:
                # while true keep on asking the user to give correct input
                while True:
                    # asking the user for an input
                    user_input_main = int(input("Please choose an option: "))
                    # if the user give the correct input then get out of the loop
                    if 0 < user_input_main <= len(options):
                        break
                    # tell the user to input inbetween these values
                    print("Please input option in between", 1, "and", len(options))
            # exception for value error
            except ValueError:
                # tell the user to input only digits
                print("Please input a digit.")
                continue

            # give confirmation
            print("Thank you for picking option " + str(user_input_main) + ".")
            print("----------------------\n")
            # break the loop
            break

        # Summary of Properties
        if user_input_main == 1:
            # number of suburb to be shown per line
            num_of_sub_shown = 5
            # total suburb
            total_len_sub = len(suburb_list_unique)
            # index suburb
            ind_sub = 0

            print("Below are the available suburb to be analyzed. ")
            # while loop to print the suburb
            while total_len_sub >= num_of_sub_shown:
                sub_small_list = suburb_list_unique[ind_sub: ind_sub + num_of_sub_shown]
                sub_small_list = [each_sub.title() for each_sub in sub_small_list]
                print(sub_small_list)
                ind_sub += num_of_sub_shown
                total_len_sub -= num_of_sub_shown
            print("----------------------\n")

        # Summary of Properties
        if user_input_main == 2:
            print("Use all to get the summary for all suburb available.")
            # modify the input
            user_input_suburb = input("Please input suburb: ").strip().lower()

            # if the suburb is all
            if user_input_suburb != "all":
                # if the input is in the data
                if user_input_suburb in suburb_list_unique:
                    # invoke the suburb_summary method
                    analyze_obj.suburb_summary(main_df, user_input_suburb)
                else:
                    print("The suburb is not available")
                    print("----------------------\n")
            else:
                # invoke the suburb_summary method
                analyze_obj.suburb_summary(main_df, user_input_suburb)

        # Average Land Size (m²)
        if user_input_main == 3:
            print("Use all to get the summary for all suburb available.")
            # modify the input
            user_input_suburb = input("Please input suburb: ").strip().lower()

            # if the user input all
            if user_input_suburb != "all":
                # if the input is in the data
                if user_input_suburb in suburb_list_unique:
                    # invoke the avg_land_size method
                    ave_val = analyze_obj.avg_land_size(main_df, user_input_suburb)
                    print("The average land in", user_input_suburb, "is", str(round(ave_val, 3)))
                else:
                    print("----------------------")
                    print("The suburb is not available")
                    print("----------------------\n")
            else:
                # invoke the avg_land_size method
                ave_val = analyze_obj.avg_land_size(main_df, user_input_suburb)
                print("The average land in all properties is", str(round(ave_val, 3)), "m²")
                print("----------------------\n")

        # Property Value Distribution
        if user_input_main == 4:
            # list all of the currency
            print("Below are the available currency to be converted.")
            for cur in currency_info_list:
                print(cur)

            # modify input
            user_input_cur = input("Please input the currency (e.g. AUD): ").strip().upper()

            # modify input
            user_input_suburb = input("Please input suburb: ").strip().lower()
            # if the suburb does not exist then notify user to use all
            if user_input_suburb not in suburb_list_unique:
                if user_input_suburb == "all":
                    pass
                else:
                    print("The suburb is not available, we will be analyzing all suburb")
                    user_input_suburb = "all"

            # invoke prop_val_dist method
            analyze_obj.prop_val_distribution(main_df, user_input_suburb, user_input_cur)

        # Sales Trend
        if user_input_main == 5:
            # invoke the sales_trend method
            analyze_obj.sales_trend(main_df)
            print("The sales trend is successfully created")
            print("Please check the sales trend under the diagram folder.")
            print("The name of the sales trand: line_sales.png")

        # Locate Price
        if user_input_main == 6:
            # modify input
            user_input_suburb = input("Please input suburb: ").strip().lower()
            # if the input is not in the data
            if user_input_suburb in suburb_list_unique:
                user_input_price = 0
                # while true
                while True:
                    # try
                    try:
                        # ask for input
                        user_input_price = int(input("Please input price: "))
                        break
                    # if valueError
                    except ValueError:
                        print("Please input a number only.")
                        continue

                # invoke the locate_price method
                if analyze_obj.locate_price(user_input_price, main_df, user_input_suburb):
                    print("There are properties in", user_input_suburb, "which have price =", user_input_price)
                    print("-----------------")
                else:
                    print("There is no property in", user_input_suburb, "which has price =", user_input_price)
                    print("-----------------")
            else:
                print("The suburb is not in the data, please choose another one.")
                print("-----------------")

        # exit
        if user_input_main == 7:
            break


if __name__ == "__main__":
    main()

# data_dir = "./property_information.csv"
# data_obj = Data()
# main_df = data_obj.extract_property_info(data_dir)
# print(len(main_df))
# the output should be 118771

# options = [
#     "1. List of suburb",
#     "2. Summary of Properties"]
# m_menu = MainMenu(options)
# print(m_menu)
# the output should be
# 1. List of suburb
# 2. Summary of Properties

# analyze_obj = DataVisual()
# print(analyze_obj.currency_exchange(main_df, 1))
# the output should be [1930000.  810000. 1762000. ... 1516000. 1340000. 1041600.]

# print(analyze_obj.suburb_filter(main_df, "clayton").head())
# the output should be
# id badge   suburb  ... auction_date  available_date  sold_date
# 0  141922512  Sold  Clayton  ...          NaN             NaN   3/4/2023
# 1  141599568  Sold  Clayton  ...          NaN             NaN   3/4/2023
# 2  141574624  Sold  Clayton  ...          NaN             NaN   1/4/2023
# 3  141840188  Sold  Clayton  ...          NaN             NaN  29/3/2023
# 4  141462600  Sold  Clayton  ...          NaN             NaN  29/3/2023

# print(analyze_obj.suburb_summary(main_df, "clayton"))
# the output should be
# bedrooms  bathrooms parking_spaces
# count  3,086.000  3,086.000      3,086.000
# mean       3.127      1.632          1.565
# std        1.585      1.112          1.102
# min        1.000      1.000          0.000
# 25%        2.000      1.000          1.000
# 50%        3.000      1.000          1.000
# 75%        4.000      2.000          2.000
# max       30.000     20.000         31.000

# print(analyze_obj.avg_land_size(main_df, "clayton"))
# the output should be 571.0422074788902

# analyze_obj.prop_val_distribution(main_df, "clayton", "USD")
# the output should be saved in the folder as hist_clayton_USD.png

# analyze_obj.sales_trend(main_df)
# the output should be saved in the folder as line_sales.png

# print(analyze_obj.locate_price(965000, main_df, "clayton"))
# the output should be True

# from algo import Algo
# algo1 = Algo()
#
# list = [1,2,3,4,5,7]
#
# list_1 = algo1.rev_insertion(list)
# print(list_1)
# the output should be [7, 5, 4, 3, 2, 1]

# target = 3
# result = algo1.recursive_bin_search(list_1, target, 0, len(list_1))
# print(result)
# the output should be True
