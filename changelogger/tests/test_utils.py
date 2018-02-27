import os

from ..utils import read_patterns


def test_read_patterns():
    filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'templates',
        'patterns.json'
    )
    patterns = read_patterns(filename)
    assert 'patterns' in patterns
