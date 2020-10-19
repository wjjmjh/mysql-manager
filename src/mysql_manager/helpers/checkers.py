def iterable(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True


def iterable_and_not_string(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        if isinstance(obj, str):
            return False
        else:
            return True


def iterable_list_of_tup_pairs(obj):
    try:
        iter(obj)
    except Exception:
        return False
    if not isinstance(obj, list):
        return False
    for tup in obj:
        if not isinstance(tup, tuple):
            return False
        if len(tup) != 2:
            return False
    else:
        return True
