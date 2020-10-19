from unittest import TestCase as orig_TestCase


class TestCase(orig_TestCase):
    def assertEqualItems(self, observed, expected, msg=None):
        """Fail if the two items contain unequal elements"""
        obs_items = list(observed)
        exp_items = list(expected)
        if len(obs_items) != len(exp_items):
            raise self.failureException(
                msg
                or "Observed and expected are different lengths: %s and %s"
                % (len(obs_items), len(exp_items))
            )

        obs_items.sort()
        exp_items.sort()
        for index, (obs, exp) in enumerate(zip(obs_items, exp_items)):
            if obs != exp:
                raise self.failureException(
                    msg
                    or "Observed %s and expected %s at sorted index %s"
                    % (obs, exp, index)
                )

    def assertSameItems(self, observed, expected, msg=None):
        """Fail if the two items contain non-identical elements"""
        obs_items = list(observed)
        exp_items = list(expected)
        if len(obs_items) != len(exp_items):
            raise self.failureException(
                msg
                or "Observed and expected are different lengths: %s and %s"
                % (len(obs_items), len(exp_items))
            )

        obs_ids = [(id(i), i) for i in obs_items]
        exp_ids = [(id(i), i) for i in exp_items]
        obs_ids.sort()
        exp_ids.sort()
        for index, (obs, exp) in enumerate(zip(obs_ids, exp_ids)):
            o_id, o = obs
            e_id, e = exp
            if o_id != e_id:  # i.e. the ids are different
                raise self.failureException(
                    msg
                    or "Observed %s <%s> and expected %s <%s> at sorted index %s"
                    % (o, o_id, e, e_id, index)
                )

    def assertContains(self, observed, item, msg=None):
        """Fail if item not in observed"""
        try:
            if item in observed:
                return
        except (TypeError, ValueError):
            pass
        raise self.failureException(
            msg or "Item %s not found in %s" % (repr(item), repr(observed))
        )

    def assertNotContains(self, observed, item, msg=None):
        """Fail if item in observed"""
        try:
            if item not in observed:
                return
        except (TypeError, ValueError):
            return
        raise self.failureException(
            msg or "Item %s should not have been in %s" % (repr(item), repr(observed))
        )

    def assertSameObj(self, observed, expected, msg=None):
        """Fail if 'observed is not expected'"""
        try:
            if observed is expected:
                return
        except Exception:
            pass
        raise self.failureException(
            msg
            or "Observed %s is not the same as expected %s"
            % (repr(observed), repr(expected))
        )

    def assertNotSameObj(self, observed, expected, msg=None):
        """Fail if 'observed is expected'"""
        try:
            if observed is not expected:
                return
        except Exception:
            pass
        raise self.failureException(
            msg
            or "Observed %s is the same as expected %s"
            % (repr(observed), repr(expected))
        )
