from mysql_manager.helpers.checkers import iterable_list_of_tup_pairs

_template1 = "CREATE TABLE {table_name} ({column_names_and_types});"


def create_query(table_name: str, column_names_and_definitions: list) -> str:
    assert isinstance(table_name, str), "table_name not string"
    assert iterable_list_of_tup_pairs(
        column_names_and_definitions
    ), "column_names_and_definitions not iterable or list of tuples of length 2)"
    return _template1.format(
        table_name=table_name,
        column_names_and_types=", ".join(
            ["{n} {t}".format(n=n, t=t) for n, t in column_names_and_definitions]
        ),
    )
