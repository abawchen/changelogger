from .elements import Commit


class Logger(object):

    def __init__(self, repo, patterns={}):
        self.repo = repo
        self.patterns = patterns
        self.commits = []

    def traverse(self, rev=None, paths='', **kwargs):
        commits = self.repo.iter_commits(rev, paths, **kwargs)
        for c in commits:
            commit = Commit(commit=c, repo_url=self.repo.url, patterns=self.patterns)
            self.commits.append(commit)
