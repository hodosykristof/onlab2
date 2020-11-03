def extract(obj, arr, key):
    """Recursively search for values of key in JSON tree."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "team":
                return arr
            if isinstance(v, (dict, list)):
                extract(v, arr, key)
            elif k == key:
                if key == "pos_x" or key == "pos_y":
                    arr.append(float(v))
                else:
                    arr.append(v)
    elif isinstance(obj, list):
        for item in obj:
            extract(item, arr, key)
    return arr


def json_extract(obj, key, data_type):
    """Recursively fetch values from nested JSON."""
    arr = []

    if data_type == "ball":
        values = extract(obj, arr, key)

    return values
