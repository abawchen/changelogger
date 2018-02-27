import pytest

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


@pytest.fixture
def mock_commit():
    commit = Mock()
    return commit


@pytest.fixture
def config():
    return {
        'patterns': {
            'Feature': '(feat)(\((.*[^\)])\))?:(.*)',
            'chore': '(chore):(.*)'
        }
    }


def test_repo_url(mock_repo, mock_urls):
    mock_repo.remote = mock_urls(['https://mockhub.com/namespace/mock.git'])
    repo = Repo(mock_repo)
    assert repo.url == 'https://mockhub.com/namespace/mock'


def test_repo_git_url(mock_repo, mock_urls):
    mock_repo.remote = mock_urls(['git@mockhub.com:namespace/mock.git'])
    repo = Repo(mock_repo)
    assert repo.url == 'https://mockhub.com/namespace/mock'


def test_commit_message_only(mock_commit):
    mock_commit.message = '\n'.join([
        'feat: This is my first feature.',
        '',
        'Commit detail description',
        '',
        'closed #11'
    ])
    commit = Commit(commit=mock_commit)
    assert commit.first_line_message == 'feat: This is my first feature.'


def test_commit_message_feat_pattern(mock_commit, config):
    mock_commit.message = '\n'.join([
        'feat: This is my second feature.'
        '',
        'Commit detail description',
        '',
        'resolved #12'
    ])
    commit = Commit(commit=mock_commit, patterns=config['patterns'])
    assert commit.category == 'Feature'
    assert commit.note == ''
    assert commit.brief == 'This is my second feature.'
