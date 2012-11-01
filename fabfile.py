import os
import sys
import functools
import logging
import webbrowser
from fabric.api import env, local

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

# Some environment information to customize
if os.name == 'posix':
    APPENGINE_PATH = '/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine'
    PYTHON = '/usr/bin/python2.7'
else:
    APPENGINE_PATH = r'C:\Program Files (x86)\Google\google_appengine'
    PYTHON = r'C:\Python27\python.exe'
APPENGINE_APP_CFG = os.path.join(APPENGINE_PATH, 'appcfg.py')

env.gae_src = os.path.dirname(__file__)

#default values
env.dryrun = False

EXTRA_PATHS = [
  APPENGINE_PATH,
  os.path.join(APPENGINE_PATH, 'lib', 'antlr3'),
  os.path.join(APPENGINE_PATH, 'lib', 'django'),
  os.path.join(APPENGINE_PATH, 'lib', 'fancy_urllib'),
  os.path.join(APPENGINE_PATH, 'lib', 'ipaddr'),
  os.path.join(APPENGINE_PATH, 'lib', 'webob'),
  os.path.join(APPENGINE_PATH, 'lib', 'yaml', 'lib'),
]

sys.path = EXTRA_PATHS + sys.path

from google.appengine.api import appinfo

def _include_appcfg(func):
    """
    Decorator that ensures the current Fabric env has a GAE app.yaml config attached to it.
    """
    @functools.wraps(func)
    def decorated_func(*args, **kwargs):
        if not hasattr(env, 'app'):
            appcfg = appinfo.LoadSingleAppInfo(open(os.path.join(env.gae_src, 'app.yaml')))
            env.app = appcfg
        return func(*args, **kwargs)
    return decorated_func

### Commands ###

def verbose():
    logger.setLevel(logging.DEBUG)

def dryrun():
    env.dryrun = True

@_include_appcfg
def deploy(tag=None):
    logger.debug(APPENGINE_APP_CFG)
    env.deploy_path = env.gae_src

    if not env.dryrun:
        logger.info('Deploying %s' % env.app.version)
        cmd = '%(python)s "%(app_cfg)s" -A %(application)s -V %(version)s --oauth2 update %(deploy_path)s' % dict(python=PYTHON, app_cfg=APPENGINE_APP_CFG, application=env.app.application, version=env.app.version, deploy_path=env.deploy_path)
        logger.debug('RUNNING %s' % cmd)
        local(cmd, capture=False)
        webbrowser.open('https://%s.appspot.com/' % env.app.application)
    else:
        logger.info('This is where we\'d actually deploy to App Engine, but this is a dryrun so we skip that part.')

def lint():
    local('pylint --rcfile=.pylintrc app')
