A defaultdict whose default factory receives the key as a parameter:

    >>> d = defaultdict2(lambda k: k + 1)
    >>> d[5]
    6

To see fancy colors (and run some tests), run:

    lettuce
