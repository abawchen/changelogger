from .elements import Commit


class Logger(object):

    def __init__(self, repo, patterns={}):
        self.repo = repo
        self.patterns = patterns
        self.commits = []
        self.tags = []

    def fetch_tags(self, start=None, end=None):
        # TODO: Refactor
        tags = self.repo.tags
        start = start or tags[0].name
        end = end or tags[-1].name
        found = False
        for tag in tags:
            if tag.name == start:
                found = True
                self.tags.append(tag)
                if start == end:
                    break
            elif found and tag.name != end:
                self.tags.append(tag)
            elif tag.name == end:
                self.tags.append(tag)
                break

    def traverse(self, rev=None, paths='', **kwargs):
        commits = self.repo.iter_commits(rev, paths, **kwargs)
        for c in commits:
            commit = Commit(commit=c, repo_url=self.repo.url, patterns=self.patterns)
            self.commits.append(commit)
