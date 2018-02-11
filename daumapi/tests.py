from search import Search
from nose.tools import assert_equal


class TestA(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    def test_init(self):
        search = Search('book')
        res = search.request(keyword='hi')
        import ipdb; ipdb.set_trace()
        assert_equal(1, 1)
