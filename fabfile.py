from fabric.api import local, task


@task
def clean():
    local("rm -rf .eggs build cryptoportfolio.egg-info dist .mypy_cache")


@task
def test():
    local("flake8 .")
    local("mypy --ignore-missing-imports .")
    local("python3 setup.py test")


@task
def install():
    local("python3 setup.py install")


@task
def dist():
    local("python3 setup.py sdist")


@task
def upload():
    unstaged_changes = local("git status -s", capture=True).stdout.strip()
    if unstaged_changes:
        raise ValueError("Tree has uncommited changes, commit first")

    clean()
    dist()
    version = local("python3 setup.py -V", capture=True).stdout.strip()
    local("twine upload dist/*")
    local("git tag -f %s" % version)
    local("git push origin --tags")
