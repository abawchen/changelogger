import re

from itertools import ifilter


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

    def __init__(self, commit, repo_url=None, patterns={}):
        self.commit = commit
        self.repo_url = repo_url
        self.first_line_message = commit.message.splitlines()[0].strip()
        self.category = ''
        self.scope = ''
        self.brief = self.first_line_message
        next(ifilter(None, (self.parse(kv) for kv in patterns.items())), None)

    @property
    def url(self):
        return '/'.join([self.repo_url, 'commit', self.commit.hexsha])

    def parse(self, kv):
        matches = re.search(kv[1], self.brief)
        if matches:
            self.meta = matches.groups()
            self.category = kv[0]
            self.scope = self.meta[2] or ''
            self.brief = self.meta[-1].strip()
            return True

        return False
