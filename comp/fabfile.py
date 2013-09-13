from fabric.contrib.files import append, exists, sed
from fabric.api import *
import os

# set up location and virtualenv 

def _cd_project_root():
    """Cd to the project directory"""
    assert hasattr(env, 'project_path')
    return cd(env.project_path)

def _activate():
    """Add a virtualenv activation prefix"""
    assert hasattr(env, 'project_path')
    assert hasattr(env, 'virtualenv')
    return prefix('source {}/bin/activate'.format(env.virtualenv))


# Set up env data

def server(server):
    env.hosts = [server]

def env(venv):
    env.virtualenv = venv

def path(path):
    env.project_path = path

def repo(repo):
    env.repo_url = repo



# git operations

def git_pull(remote='origin', branch='master'):
    """ Pull the last version from the git repository to the set branch"""
    assert hasattr(env, 'project_path')
    with _cd_project_root():
        run('git pull {} {}'.format(remote, branch))

def git_clone():
    """ Clone the given repository to the project path"""
    assert hasattr(env, 'project_path')
    assert hasattr(env, 'repo_url')
    run('git clone {} {}'.format(env.repo_url, env.project_path))

def git_tag_now(prefix):
    """ Tag the current branch HEAD with prefix+timestamp"""
    import datetime
    assert hasattr(env, 'project_path')
    with _cd_project_root():
        run('git tag {}-{}'.format(prefix, datetime.datetime.now().strftime(
            '-%Y-%m-%d-%H-%M-%S'))
        )

# basic helper functions

def manage(command):
    """Run python manage `command`"""
    with _activate():
        with _cd_project_root():
            run('python manage.py {}'.format(command))

def install_requirements():
    """Install required python packages, from requirements.txt"""
    with _cd_project_root():
        with _activate():
            run('pip install -r requirements.txt')

def collectstatic():
    """Collect static files"""
    manage('collectstatic --noinput')

def syncdb():
    """Execute initial syncdb"""
    manage('syncdb')

def migrate():
    """Execute any pending South migration"""
    manage('migrate')


# high level commands

def setup():
    """Create an initial deployment from source git repo.
       Also creates a sample settings/local.py which just pulls all
       the settings from dev.py
    """
    assert hasattr(env, 'project_path')
    assert hasattr(env, 'virtualenv')
    assert hasattr(env, 'repo_url')
    git_clone()
    git_tag_now('initial-deploy')
    project_name = 'comp'
    fname = '{project}/{project}/settings/local.py'.format(
            project=project_name
            )
    with _cd_project_root():
        run('test -f {fname} || echo "from .dev import *" >> {fname}'.format(
            fname=fname)
        )
        run('virtualenv --no-site-packages {}'.format(env.virtualenv))
    update()
    # test()

def update():
    """Update an existing deployment"""
    install_requirements()
    collectstatic()
    syncdb()
    migrate()

def deploy():
    """Deploy a new version of the app from the tracked branch"""
    assert hasattr(env, 'project_path')
    assert hasattr(env, 'virtualenv')
    git_pull()
    git_tag_now('deploy')
    update()
    # test()

try:
    from local_fabfile import *
except ImportError:
    pass

