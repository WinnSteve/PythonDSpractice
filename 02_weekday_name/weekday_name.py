def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # need a variable with the days of the week starting with Sunday bc of example above
    days = ['Sunday', 'Monday', 'Tuesday',
            'Wednesday', 'Thurday', 'Friday', 'Saturday']

    # if day entered is less than 1 or greater than 7 ot woll return None
    if day_of_week < 1 or day_of_week > 7:
        return None

    # need to have the minus one otherwise it will not return the proper corresponding day
    return days[day_of_week - 1]
