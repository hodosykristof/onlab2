def extract(obj, arr, key):
    """Recursively search for values of key in JSON tree (ball)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "team":
                # arr.append('players:')
                # extract_players(v, arr, key)
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


def extract_players(obj, arr, key):
    """Recursively search for values of key in JSON tree (player)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "name":
                arr.append(v)
            if isinstance(v, (dict, list)):
                extract_players(v, arr, key)
            elif k == key:
                if key == "pos_x" or key == "pos_y":
                    arr.append(float(v))
                else:
                    arr.append(v)
    elif isinstance(obj, list):
        for item in obj:
            extract_players(item, arr, key)
    return arr


def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    values = extract(obj, arr, key)

    return values


def extract_all(obj, arr_x, arr_y, arr_sec, arr_half):
    """Recursively search for values of x, y and video second in JSON tree, returns them in different arrays (ball). """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "team":
                arr_x.append('players:')
                arr_y.append('players:')
                arr_sec.append('players:')
                arr_half.append('players:')
                extract_players_all(v, arr_x, arr_y, arr_sec, arr_half)
                return arr_x, arr_y, arr_sec, arr_half
            if isinstance(v, (dict, list)):
                extract_all(v, arr_x, arr_y, arr_sec, arr_half)
            elif k == "pos_x":
                arr_x.append(float(v))
            elif k == "pos_y":
                arr_y.append(float(v))
            elif k == "video_second":
                arr_sec.append(int(float(v)))
            elif k == "half":
                arr_half.append(int(v))
    elif isinstance(obj, list):
        for item in obj:
            extract_all(item, arr_x, arr_y, arr_sec, arr_half)
    return arr_x, arr_y, arr_sec, arr_half


def extract_players_all(obj, arr_x, arr_y, arr_sec, arr_half):
    """Recursively search for values of x, y and video second in JSON tree (player)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "name":
                arr_x.append(v)
                arr_y.append(v)
                arr_sec.append(v)
                arr_half.append(v)
            if isinstance(v, (dict, list)):
                extract_players_all(v, arr_x, arr_y, arr_sec, arr_half)
            elif k == "pos_x":
                arr_x.append(float(v))
            elif k == "pos_y":
                arr_y.append(float(v))
            elif k == "video_second":
                arr_sec.append(int(float(v)))
            elif k == "half":
                arr_half.append(int(v))
    elif isinstance(obj, list):
        for item in obj:
            extract_players_all(item, arr_x, arr_y, arr_sec, arr_half)
    return arr_x, arr_y, arr_sec, arr_half


def json_extract_all(obj):
    """Recursively fetch values from nested JSON."""
    arr_x = []
    arr_y = []
    arr_sec = []
    arr_half = []

    values_x, values_y, values_sec, values_half = extract_all(obj, arr_x, arr_y, arr_sec, arr_half)

    return values_x, values_y, values_sec, values_half
