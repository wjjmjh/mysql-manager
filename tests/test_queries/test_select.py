from mysql_manager.helpers.testers import TestCase
from mysql_manager.queries.select import select_query


class SelectQueryTests(TestCase):
    def test_select_query(self):
        table = "test_tbl"
        # tests the most basic case that all columns and no distinct.
        got1 = select_query(table=table)
        self.assertEqual(got1, "SELECT * FROM test_tbl;")
