from mysql_manager.helpers.testers import TestCase
from mysql_manager.queries.create import create_query


class CreateQueryTests(TestCase):
    test_table_name_1 = "test_tbl_shop"
    test_column_names_and_definitions = [("A","int"), ("B", "text"), ("C", "NULL")]

    def test_create_querys(self):
        # tests column specified
        got1 = create_query(
            table_name=self.test_table_name_1, column_names_and_definitions=self.test_column_names_and_definitions
        )
        self.assertEqual(
            got1, "CREATE TABLE test_tbl_shop (A int, B text, C NULL);"
        )
        got2 = create_query(
            table_name=self.test_table_name_1, column_names_and_definitions=[self.test_column_names_and_definitions[1]]
        )
        self.assertEqual(got2, "CREATE TABLE test_tbl_shop (B text);"
        )

    def test_create_bad_params(self):
        with self.assertRaises(AssertionError):
            create_query(table_name=None, column_names_and_definitions=self.test_column_names_and_definitions[1])
        with self.assertRaises(AssertionError):
            create_query(table_name=self.test_table_name_1, column_names_and_definitions=["A","B","C"])

