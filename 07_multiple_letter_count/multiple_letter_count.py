def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # make a new dict
    sample = {}

    # use a for in and the .get method where it adds one for each ltr

    for ltr in phrase:
        sample[ltr] = sample.get(ltr, 0) + 1

    return sample
