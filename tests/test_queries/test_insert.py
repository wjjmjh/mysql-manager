from mysql_manager.helpers.testers import TestCase
from mysql_manager.queries.insert import insert_query, multipe_insert_query


class InsertQueryTests(TestCase):
    def test_insert_query(self):
        table = "test_tbl"
        columns = ["c1", "c2", "c3"]
        values = ["v1", "v2", "v3"]
        # tests column specified
        got1 = insert_query(
            columns_specified=True, table=table, columns=columns, values=values
        )
        self.assertEqual(
            got1, 'INSERT INTO test_tbl (c1, c2, c3) VALUES ("v1", "v2", "v3");'
        )
        # tests column not specified
        got2 = insert_query(
            columns_specified=False, table=table, columns=columns, values=values
        )
        self.assertEqual(got2, 'INSERT INTO test_tbl VALUES ("v1", "v2", "v3");')
