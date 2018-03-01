import pytest

from mock import MagicMock as Mock

from .fixtures import config, setup_repo
from ..elements import Repo
from ..logger import Logger

url = 'https://mockhub.com/namespace/mock'


@pytest.fixture
def repo():
    git_repo = setup_repo()
    repo = Repo(repo=git_repo, url=url)
    return repo


def test_logger(repo, config):
    logger = Logger(repo=repo, patterns=config['patterns'])
    logger.traverse()

    expected = [
        Mock(
            repo_url=url,
            category='Docs',
            scope='README',
            brief='The latest commit'
        ),
        Mock(
            repo_url=url,
            category='Fix',
            scope='',
            brief='Typo of hexsha'
        ),
        Mock(
            repo_url=url,
            category='Chore',
            scope='',
            brief='Initial commit'
        )
    ]
    for commit, mock in zip(logger.commits, expected):
        assert commit.repo_url == mock.repo_url
        assert commit.brief == mock.brief
        assert commit.category == mock.category
        assert commit.scope == mock.scope


