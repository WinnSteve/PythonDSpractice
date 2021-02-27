def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """

    # no need to write an else statement because functions default return is None
    # returns list[-1] which no matter the length will always display last item, found this on StackOverflow
    if lst:
        return lst[-1]
