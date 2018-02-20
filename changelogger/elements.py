import re

from re import match



class Repo(object):

    def __init__(self, repo, url=None):
        self._repo = repo
        self._url = url

    @property
    def url(self):
        if self._url is None:
            self._url = self._repo.remote().urls.next()
            if not self._url.startswith('http'):
                self._url = self._url.replace(':', '/').replace('git@', 'https://')
            if self._url.endswith('.git'):
                self._url = re.sub('\.git', '', self._url)
        return self._url

class Commit(object):

    def __init__(self, commit, repo_url, pattern=None):
        self.commit = commit
        self.repo_url = repo_url
        self.first_line_message = commit.message.splitlines()[0].strip()

        if pattern is not None:
            self.meta = match(pattern, self.first_line_message)

    @property
    def url(self):
        return '/'.join([self, repo_url, 'commit', self._commit.hexsha])
