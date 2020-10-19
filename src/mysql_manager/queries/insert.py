from mysql_manager.helpers.checkers import iterable
from mysql_manager.helpers.general import iterable_to_string
from mysql_manager.queries import wrap

_template1 = "INSERT INTO {table} ({columns}) VALUES ({values});"
_template2 = "INSERT INTO {table} VALUES ({values});"
_template3 = "INSERT INTO {table} ({columns}) VALUES {value_tuples};"
_template4 = "INSERT INTO {table} VALUES {value_tuples};"
_template5 = "INSERT INTO {tableB} SELECT * FROM {tableA};"


def append_query(tableA, tableB):
    return _template5.format(tableA=wrap(tableA), tableB=wrap(tableB))


def _with_columns(table, columns, values, single_query=True):
    if iterable(columns):
        columns = iterable_to_string(columns)

    if iterable(values):
        values = iterable_to_string(values, wrapped=True)

    if single_query:
        return _template1.format(table=table, columns=columns, values=values)
    return _template3.format(table=table, columns=columns, value_tuples=values)


def _without_columns(table, values, single_query=True):
    if iterable(values):
        values = iterable_to_string(values, wrapped=True)

    if single_query:
        return _template2.format(table=table, values=values)
    return _template4.format(table=table, value_tuples=values)


def insert_query(columns_specified=True, **kwargs):
    """
    :param columns_specified: if inserting into specified fields or not
    :param kwargs: table, columns(optional), values
    :return: a constructed inserting sql query
    """
    if columns_specified:
        return _with_columns(kwargs["table"], kwargs["columns"], kwargs["values"])
    else:
        return _without_columns(kwargs["table"], kwargs["values"])


def multipe_insert_query(columns_specified=True, **kwargs):
    """
    kwargs["rows"] could be a two dimensional array
    """
    rows = kwargs["rows"]
    try:
        not iterable(rows[0][0])
    except Exception:
        assert "rows has to be a two dimensional array."

    values = ", ".join(
        ["({})".format(", ".join([wrap(ele) for ele in row])) for row in rows]
    )
    if columns_specified:
        return _with_columns(
            kwargs["table"], kwargs["columns"], values, single_query=False
        )
    else:
        return _without_columns(kwargs["table"], values, single_query=False)
