import os


def _wrapping_refreshing(func):
    def wrapped(self):
        got = func(self)
        self.refresh_base()
        return got

    return wrapped


class repoPathManager:
    def __init__(self):
        self.base = ""

    def refresh_base(self):
        self.base = ""

    def _combine_one(self, component):
        self.base = os.path.join(self.base, component)

    def combine(self, *directed_folders):
        for folder in directed_folders:
            self._combine_one(folder)
        got = self.base
        self.refresh_base()
        return got

    def find_root(self):
        explore = str(os.path.dirname(os.path.abspath(__file__))).split(os.sep)
        self.base = os.path.sep.join(explore[: explore.index("mysql-manager") + 1])
        return self

    def find_src(self):
        explore = str(os.path.dirname(os.path.abspath(__file__))).split(os.sep)
        self.base = os.path.sep.join(explore[: explore.index("src") + 1])
        return self

    def find_mysql_manager(self):
        explore = str(os.path.dirname(os.path.abspath(__file__))).split(os.sep)
        self.base = os.path.sep.join(explore[: explore.index("mysql_manager") + 1])
        return self

    @property
    @_wrapping_refreshing
    def exe(self):
        self.find_src()
        return self.combine("mysql_manager", "exe")

    @property
    @_wrapping_refreshing
    def mysql_manager(self):
        self.find_mysql_manager()
        return self.base

    @property
    @_wrapping_refreshing
    def test_data(self):
        self.find_root()
        return self.combine("tests", "data")
