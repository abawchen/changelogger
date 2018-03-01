from git import Repo

import os.path as osp
import pytest
import shutil

join = osp.join
rw_dir = osp.dirname(osp.realpath(__file__))

def setup_repo():
    repo_dir = join(rw_dir, 'bare-repo')
    shutil.rmtree(repo_dir, ignore_errors=True)

    repo = Repo.init(repo_dir)

    filename = osp.join(repo_dir, 'README.md')
    open(filename, 'wb').close()
    repo.index.add([filename])
    repo.index.commit('chore: Initial commit')
    repo.create_tag('v0.0.1', message='Alpha release')

    with open(filename, 'a') as f:
        f.write('Hello World\n')
    repo.index.add([filename])
    repo.index.commit('fix: Typo of hexsha')
    repo.create_tag('v0.0.2', message='Stage release')

    with open(filename, 'a') as f:
        f.write('Update README\n')
    repo.index.add([filename])
    repo.index.commit('docs(README): The latest commit')
    repo.create_tag('v1.0.0', message='Production release')

    return repo


@pytest.fixture
def config():
    return {
        'patterns': {
            'Chore': '(chore):(.*)',
            'Feature': '(feat)(\((.*[^\)])\))?:(.*)',
            'Fix': '(fix)(\((.*[^\)])\))?:(.*)',
            'Docs': '(docs)(\((.*[^\)])\))?:(.*)',
        }
    }
