# Name: Yehezkiel Efraim Darmadi
# Student ID: ydar0001
# Student No: 34078215

# create class to use the algorithm
class Algo:
    """
    A class for algorithm.


    Attributes
    ----------

    Methods
    -------
    rev_insertion()
        return a list of sorted list using reverse insertion method
    recursive_bin_search()
        return the target index.
    """
    def rev_insertion(self, lst):
        """
        return a list of sorted list using reverse insertion method.

        Returns
        ----------
        list
            list of sorted list.
        """
        # start at index 1
        for i in range(1, len(lst)):
            # declare the number which we want to check
            key = lst[i]
            # left number beside the key
            j = i - 1
            # while loop with condition j needs to be within the index and the key> than the number
            while j >= 0 and lst[j] < key:
                # the correct number is less than key then replace the value in the right index with the current number
                lst[j + 1] = lst[j]
                # make index smaller
                j -= 1
            # if the current num is greater than key or index is out of bound, replace the current with they key
            lst[j + 1] = key

        # return key
        return lst

    def recursive_bin_search(self, lst, target, low, high):
        """
        check whether a price is in the list.

        Returns
        ----------
        bool
            True if found.
        """
        # if target not found return false
        if low > high:
            return False

        # Calculate the middle index
        mid = low + (high - low) // 2

        # Target found, return True
        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            # If the middle element is greater than the target, search the low half
            return self.recursive_bin_search(lst, target, mid + 1, high)
        else:
            # If the middle element is less than the target, search the high half
            return self.recursive_bin_search(lst, target, low, mid - 1)