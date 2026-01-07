import pytest
from tests.core import parse_tests, get_output, is_equal, MAX_TIME
import submission


@pytest.mark.timeout(MAX_TIME)
@pytest.mark.parametrize(("inp", "expected"), parse_tests(submission.__doc__))
def test_submission(inp, expected):
    result = get_output(inp, submission.main)
    assert is_equal(result, expected)
