# -*- coding: utf-8 -*-

import environ
from fabric.api import cd, env, local, run, task
from fabric.contrib import project

# env.hosts = ['ubuntu@140.143.243.241']
env.hosts = ['root@103.200.97.197']

env.excludes = (
    "*.pyc", "*.db", ".DS_Store", ".coverage", ".git", ".hg", ".tox", ".idea/",
     'runtime/', 'tests', 'docs', '__pycache__',
    'env.docker', 'env.server', 'docs')

env.remote_dir = '~/sensor/server'
env.local_dir = '.'

def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

@task
def ws():
    '''run websocket'''
    local('daphne -b 0.0.0.0 -p 8080 config.asgi:application')

@task
def plan(action='check'):
    '''crontab'''
    local('python schedule.py {}'.format(action))

@task
def lint():
    '''python 代码风格校验'''
    local('''pycodestyle **/*.py''')


@task
def su(fixture=0):
    '''创建超级用户'''
    if fixture == 0:
        local('python manage.py createsuperuser --email ibopo@126.com --username bopo')
    else:
        local('python manage.py createsuperuser')

@task
def dev():
    '''运行开发服务器'''
    local('python manage.py runserver')


@task
def test():
    ''' 执行项目代码测试 '''
    local('py.test -v')

@task
def cov():
    ''' 测试代码覆盖率 '''
    local('python manage.py jenkins --settings=config.settings.test --enable-coverage --coverage-format html -v2')
    local('open reports/coverage/index.html')

@task
def seed(app=''):
    '''填充 mock 数据'''
    app = '_{}'.format(app) if app else ''
    local('python manage.py runscript seeds{} -v3'.format(app))


@task(alias='mm')
def mkmg(app=''):
    '''数据库 migration 操作'''
    local('python manage.py makemigrations {app}'.format(app=app))
    local('python manage.py migrate')


@task
def load(name='all'):
    ''' 导入开发数据 '''
    local('python manage.py loaddata config/fixtures/{}.json'.format(name))


@task
def dump(app=''):
    ''' 导出开发数据 '''
    local('python manage.py dumpdata {} > config/fixtures/{}.json'.format(
        app, (app if app else 'all')))


@task
def comp(mode='pre'):
    '''更新 requirements.txt 内的版本'''
    local('pip-compile --output-file requirements.{mode}.txt requirements/{mode}.txt --trusted-host mirrors.aliyun.com '.format(mode=mode))


@task
def wsgi(worker='egg:meinheld#gunicorn_worker', host='127.0.0.1', port=5000):
    ''' 启动 wsgi 服务'''
    settings = 'DJANGO_SETTINGS_MODULE=config.settings.pre'
    local('{settings} gunicorn config.wsgi:application -k {worker} -w 4 -b {host}:{port}'.format(
            worker=worker, host=host, port=port, settings=settings))


@task
def sort():
    ''' 整理文件导入格式'''
    local('isort **/*.py')

@task
def unix():
    '''文本文件 windows 格式转 unix 格式'''
    local('find . "*.txt" | xargs dos2unix')
    local('find . "*.md" | xargs dos2unix')
    local('find . "*.py" | xargs dos2unix')
    local('dos2unix Makefile')


@task(alias='ci')
def gc():
    '''提交源码仓库(git commit)'''
    local('git commit -m "first commit"')


@task
def gp(branch='develop'):
    '''推送源码仓库(git push)'''
    local('git push -u origin {}'.format(branch))


@task
def stat():
    '''更新静态文件'''
    with cd(env.remote_dir):
        run('python manage.py collectstatic --noinput')


@task
def lst():
    '''更新静态文件'''
    local('python manage.py collectstatic --noinput')


@task
def push():
    '''同步服务器代码'''
    project.rsync_project(
        remote_dir=env.remote_dir,
        local_dir=env.local_dir,
        exclude=env.excludes,
        delete=False
    )


@task
def migr():
    '''合并数据文件'''
    with cd(env.remote_dir):
        run('''python manage.py migrate''')


# @task()
# def init():
#     '''初始化服务'''

#     project.rsync_project(
#         remote_dir=env.remote_dir,
#         local_dir=env.local_dir,
#         exclude=env.excludes,
#         delete=True
#     )

#     run('/usr/bin/supervisorctl device start')


@task()
def rest():
    '''重启服务'''
    run('sudo /etc/init.d/supervisor restart')


@task
def stop():
    '''停止服务'''
    run('sudo /etc/init.d/supervisor stop')


@task
def prod():
    '''文件打包'''
    local('tar zcfv ./prod.tgz '
          '--exclude=.git '
          '--exclude=.tox '
          '--exclude=.svn '
          '--exclude=.env '
          '--exclude=.idea '
          '--exclude=*.tgz '
          '--exclude=*.pyc '
          '--exclude=.vagrant '
          '--exclude=tests '
          '--exclude=assets/media/* '
          '--exclude=assets/static/* '
          '--exclude=runtime/* '
          '--exclude=vendors '
          '--exclude=config/fixtures '
          '--exclude=env.* '
          '--exclude=.DS_Store '
          '--exclude=.phpintel '
          '--exclude=.template '
          '--exclude=db.sqlite3 '
          '--exclude=Makefile '
          '--exclude=pytest.ini '
          '--exclude=README.md '
          '--exclude=Pipfile '
          '--exclude=Pipfile.lock '
          '--exclude=fabfile.py '
          '--exclude=Vagrantfile .')


@task
def pack():
    '''文件打包'''
    local('tar zcfv ./pack.tgz '
          '--exclude=.git '
          '--exclude=.tox '
          '--exclude=.env '
          '--exclude=.idea '
          '--exclude=*.tgz '
          '--exclude=*.pyc '
          '--exclude=.vagrant '
          '--exclude=assets/media/* '
          '--exclude=assets/static/* '
          '--exclude=runtime/* '
          '--exclude=.DS_Store '
          '--exclude=.phpintel '
          '--exclude=.template '
          '--exclude=db.sqlite3 '
          '--exclude=Vagrantfile .')
