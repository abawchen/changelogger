import re

# https://stackoverflow.com/a/33715649/9041712
try:
    from future_builtins import filter
except ImportError:
    pass


class Repo(object):

    def __init__(self, repo, url=None):
        self._repo = repo
        self._url = url

    @property
    def url(self):
        if self._url is None:
            self._url = next(self._repo.remote().urls)
            if not self._url.startswith('http'):
                self._url = self._url.replace(':', '/').replace('git@', 'https://')
            if self._url.endswith('.git'):
                self._url = re.sub('\.git', '', self._url)

        return self._url

    def iter_commits(self, rev=None, paths='', **kwargs):
        return self._repo.iter_commits(rev, paths, **kwargs)


class Commit(object):

    def __init__(self, commit, repo_url=None, patterns={}):
        self._commit = commit
        self.repo_url = repo_url
        self.first_line_message = commit.message.splitlines()[0].strip()
        self.category = ''
        self.scope = ''
        self.brief = self.first_line_message
        next(filter(None, (self.parse(kv) for kv in patterns.items())), None)

    @property
    def url(self):
        return '/'.join([self.repo_url, 'commit', self._commit.hexsha])

    def parse(self, kv):
        matches = re.search(kv[1], self.brief)
        if matches:
            self.meta = matches.groups()
            self.category = kv[0]
            self.scope = self.meta[2] or ''
            self.brief = self.meta[-1].strip()
            return True

        return False
