from mock_decorator import mock_decorator

@mock_decorator
def test_reproduction():
    assert 1 == 1
