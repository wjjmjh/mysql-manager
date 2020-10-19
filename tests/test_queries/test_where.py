from mysql_manager.helpers.testers import TestCase
from mysql_manager.queries.where import where


class WhereConstraintsTests(TestCase):
    def test_where_constraint(self):
        # tests AND logic operator
        and_constraints = ["A > B", "B > C", "C > D or D > E"]
        self.assertEqual(
            where(and_constraints), "WHERE (A > B) AND (B > C) AND (C > D OR D > E)"
        )
        or_constraints = ("A > B", "B > C", "C > D and D > E")
        self.assertEqual(
            where(or_constraints), "WHERE (A > B) OR (B > C) OR (C > D AND D > E)"
        )
