from mysql_manager.queries import wrap


def iterable_to_string(iterable, deliminator=", ", wrapped=False):
    if wrapped:
        return deliminator.join([wrap(v) for v in iterable])
    return deliminator.join(iterable)
