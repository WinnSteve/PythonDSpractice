def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    count = {}

    # create a frequency counter of num
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # variable using the max method

    high_val = max(count.values())

    # index highest value and return the number which appeared the most

    for(num, freq) in count.items():
        if freq == high_val:
            return num
