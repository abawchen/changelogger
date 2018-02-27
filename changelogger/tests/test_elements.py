import pytest

from git import Repo as GitGepo
from git import Commit as GitCommit
from mock import MagicMock as Mock

from ..elements import Commit, Repo

@pytest.fixture
def mock_repo():
    repo = Mock()
    return repo


@pytest.fixture
def mock_urls():
    urls_mock = Mock()

    def urls(lst):
        urls_mock.urls = ((url) for url in lst)
        return Mock(return_value=urls_mock)
    return urls

def test_commit():
    pass


def test_repo_url(mock_repo, mock_urls):
    mock_repo.remote = mock_urls(['https://mockhub.com/namespace/mock.git'])
    repo = Repo(mock_repo)
    assert repo.url == 'https://mockhub.com/namespace/mock'


def test_repo_git_url(mock_repo, mock_urls):
    mock_repo.remote = mock_urls(['git@mockhub.com:namespace/mock.git'])
    repo = Repo(mock_repo)
    assert repo.url == 'https://mockhub.com/namespace/mock'

