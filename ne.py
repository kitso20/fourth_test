def flatten_nested_list(nested):
    """Flatten a nested list of arbitrary depth using recursion."""
    li = []
    for item in nested:
        if isinstance(item,list):
            li.extend(flatten_nested_list(item))
        else:
            li.append(item)
        
    return li
        
print(flatten_nested_list([1, [2, [3, 4]], 5]))