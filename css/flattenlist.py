def flatten_recursive(nested_list):
    """Recursively flattens a nested list of any depth."""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            # If the item is a list, extend the flattened list with the result of a recursive call
            flattened.extend(flatten_recursive(item))
        else:
            # Otherwise, it's a single element, so just append it
            flattened.append(item)
    return flattened
complex_list = [1, 2, [3, [4, 5], [1, 2, [4, 5]], 7], 10]
print(flatten_recursive(complex_list))
