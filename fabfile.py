import random

from fabric.api import local, prefix, prompt
from fabric.contrib.console import confirm
ENVIRONMENTS = ['dev', 'live']


conf = {
    "env": "stage",
    "user_profile": "pointer81",
    "region": "ap-northeast-2",
    "DJANGO_SETTINGS_MODULE": "main.settings_local"}


def _do_migrate():
    with prefix(". $VIRTUAL_ENV/bin/activate"):
        local("zappa manage live  migrate")

def _do_collectstatic():
    with prefix(". $VIRTUAL_ENV/bin/activate"):
        local("zappa manage live  collectstatic")

# def flake8():
#     local("flake8 --config=setup.cfg")

# def test_code(reuse_db=0, case=''):
#     flake8()
#     local("REUSE_DB=%s DJANGO_SETTINGS_MODULE={DJANGO_SETTINGS_MODULE} python manage.py test %s "
#           "--nocapture -v 3 --noinput".format(**conf) % (reuse_db, case))


def _sanity_check(force=False):

    branch = local("git rev-parse --abbrev-ref HEAD", capture=True)

    if branch != 'master' and not force:
        print("Sanity : You are on [%s], not [master]." % branch)
        return False

    a = random.randint(1, 9)
    b = random.randint(1, 9)
    result = prompt('You\'re deploying on production. \n  %d + %d = ?' % (a, b))

    if not (int(result) == a + b):
        print("Sanity : Calm down on deploying")
        return False

    return True


def deploy(force=False, env='stage'):
    if env not in ENVIRONMENTS:
        print("The environment '%s needs to be one of %s" % (env, ENVIRONMENTS))

    res = confirm("You\'re deploying on \"%s\"." % env)

    if not res:
        return

    conf['env'] = env

    if _sanity_check(force):
        with prefix(". $VIRTUAL_ENV/bin/activate"):
            local("zappa update live")
        _do_migrate()

        local('curl https://backend-live.hoodpub.com/api/userbook/ | jq .')

    else:
        print("Failed in sanity checking.")
