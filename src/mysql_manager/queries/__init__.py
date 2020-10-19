__contributors__ = ["Stephen Ka-Wah Ma"]


def wrap(val):
    if isinstance(val, str):
        return '"{}"'.format(val)

    if isinstance(val, bool):
        return "{}".format(str(val).upper())

    return "{}".format(val)
