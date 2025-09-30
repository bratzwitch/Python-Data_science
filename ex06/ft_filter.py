def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    res = []
    for variable in iterable:
        if function(variable):
            res.append(variable)
    return res
