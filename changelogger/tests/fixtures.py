from git import Repo

import os.path as osp
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
    repo.index.commit('initial commit')

    with open(filename, 'a') as f:
        f.write('Update README\n')
    repo.index.add([filename])
    repo.index.commit('docs(README): The lastest commit')

    return repo
