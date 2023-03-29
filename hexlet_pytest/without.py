def set_(coll, path, value):
    length = len(path)
    last_index = length - 1
    index = 0
    nested = coll

    while index < length:
        key = path[index]
        new_value = value
        if index != last_index:
            obj_value = nested[key] if key in nested else None
            new_value = obj_value if isinstance(obj_value, dict) else {}
        nested[key] = new_value
        nested = nested[key]
        index += 1
    return coll