def flatten_list(nested_list):
	"""
    Flatten an arbitrarily nested list

    Parameters
    ----------
    nested_list : nested list of int
        List with item to be either integers or list
        Example: [2,[[3,[4]], 5]]

    Returns
    -------
    flat_list : list of int
        A flattened list with only integers
        Example: [2,3,4,5]
    """