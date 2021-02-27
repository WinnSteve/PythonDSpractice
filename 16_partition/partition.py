def partition(lst, fn):
    """Partition lst by predicate.

     - lst: list of items
     - fn: function that returns True or False

     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0

        >>> def is_string(el):
        ...     return isinstance(el, str)

        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]

        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    # had to consult springboard solution for this one
    # need to first create 2 new list for pass and fail

    pass_list = []
    fail_list = []

    # run for in loop to match items as true and false and seperate them into their new lists
    for val in lst:
        if fn(val):
            pass_list.append(val)
        else:
            fail_list.append(val)

    return [pass_list, fail_list]
