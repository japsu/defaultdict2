A defaultdict whose default factory receives the key as a parameter:

    >>> from defaultdict2 import defaultdict2
    >>> d = defaultdict2(lambda k: k + 1)
    >>> d[5]
    6
    >>> dict(d)
    {5: 6}

To see fancy colors (and run some tests), run:

    lettuce

You could also check the examples in this file:

    python -m doctest README.md
