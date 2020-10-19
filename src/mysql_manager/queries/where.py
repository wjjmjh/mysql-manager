from mysql_manager.helpers.checkers import iterable

_template = "WHERE {constraints}"


def where(constraints):
    """
    constraints is an iterable of strings(constraints), for example:

    ["A > B", "B > C", "C > D or D > E"] (case 1)
    or
    ("A > B", "B > C", "C > D and D > E") (case 2)

    notes that, if the input is array data structure, constraints will be joined using "AND" (case 1),
    otherwise, "OR" (case 2)
    """
    assert iterable(constraints), "constraints is supposed to be iterable."
    if len(constraints) == 0:
        return ""
    constraints = constraints.__class__(
        ["({})".format(cons.upper()) for cons in constraints]
    )
    if isinstance(constraints, list):
        return _template.format(constraints=" AND ".join(constraints))
    return _template.format(constraints=" OR ".join(constraints))
