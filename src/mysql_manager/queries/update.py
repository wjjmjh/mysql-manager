from mysql_manager.queries import wrap

_template1 = "UPDATE {table} SET {target_column}={target_value} WHERE {base_column}={base_value};"


def update_query(table_name, target_col, target_val, base_col, base_val):
    return _template1.format(
        table=table_name,
        target_column=target_col,
        target_value=wrap(target_val),
        base_column=base_col,
        base_value=wrap(base_val),
    )
