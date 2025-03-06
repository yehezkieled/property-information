# Name: Yehezkiel Efraim Darmadi
# Student ID: ydar0001
# Student No: 34078215

# create class to display main menu
class MainMenu:
    """
    A class used to print main menu


    Attributes
    ----------
    options : list
        a list of options

    Methods
    -------
    str()
        return the option formatted string.
    """
    # the constructor
    def __init__(self, options):
        """
        Parameters
        ----------
        retailer_id : list
            list that store options
        """
        self.options = options

    # method to print the options
    def __str__(self):
        """
        generate the main menu formatted string

        Returns
        ----------
        str
            the main menu information.
        """
        return "\n".join(self.options)

