def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """

    # need to ensure the input of the word and letter will be changed to lowercase to avoid any confusion and use the .count built in method
    return word.lower().count(letter.lower())
