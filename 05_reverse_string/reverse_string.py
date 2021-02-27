def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    # found this handy trick on geeksforgeeks
    # solution has an even more simple method I need to look up to understand better
    if len(phrase) == 0:
        return phrase
    else:
        return reverse_string(phrase[1:]) + phrase[0]
