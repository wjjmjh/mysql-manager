from mysql_manager.helpers.checkers import iterable
from mysql_manager.queries import wrap
from mysql_manager.queries.where import where

_template1 = "SELECT {columns} FROM {table};"
_template2 = "SELECT {columns} FROM {table} {where};"
_template3 = "SELECT DISTINCT {columns} FROM {table};"
_template4 = "SELECT DISTINCT {columns} FROM {table} {where};"
_template5 = "SELECT {columns} FROM {table} ORDER BY {orders};"
_template6 = "SELECT {columns} FROM {table} {where} ORDER BY {orders};"
_template7 = "SELECT DISTINCT {columns} FROM {table} ORDER BY {orders};"
_template8 = "SELECT DISTINCT {columns} FROM {table} {where} ORDER BY {orders};"


def select_query(table, columns="*", distinct=False):
    if iterable(columns):
        columns = ", ".join(columns)
    if distinct:
        return _template3.format(columns=columns, table=table)
    return _template1.format(columns=columns, table=table)


def select_where_query(table, columns="*", distinct=False, constraints=None):
    if constraints is None:
        constraints = []
    if iterable(columns):
        columns = ", ".join(columns)
    if distinct:
        return _template4.format(columns=columns, table=table, where=where(constraints))
    return _template2.format(columns=columns, table=table, where=where(constraints))


def select_order_by_query(table, columns="*", distinct=False, orders=None):
    if orders is None:
        orders = []
    assert iterable(orders), "orders is supposed to be iterable."
    if iterable(columns):
        columns = ", ".join(columns)
    if distinct:
        return _template3.format(columns=columns, table=table, orders=", ".join(orders))
    return _template1.format(columns=columns, table=table, orders=", ".join(orders))


def select_where_order_by_query(
    table, columns="*", distinct=False, constraints=None, orders=None
):
    if orders is None:
        orders = []
    assert iterable(orders), "orders is supposed to be iterable."

    if constraints is None:
        constraints = []
    if iterable(columns):
        columns = ", ".join(columns)
    if distinct:
        return _template4.format(
            columns=columns,
            table=table,
            where=where(constraints),
            orders=", ".join(orders),
        )
    return _template2.format(
        columns=columns, table=table, where=where(constraints), orders=", ".join(orders)
    )
