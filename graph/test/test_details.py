from ..details import msg


class TestDetails(object):
    def test_msgText(self):
        x = msg()
        assert 'Fala tu' in x

    def test_msgType(self):
        x = msg()
        assert type(x) is str
