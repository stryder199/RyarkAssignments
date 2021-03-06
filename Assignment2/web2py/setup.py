#!/usr/bin/env python

from distutils.core import setup
from gluon.fileutils import tar,untar
import tarfile
import sys

def tar(file, filelist, expression='^.+$'):
    """
    tars dir/files into file, only tars file that match expression
    """

    tar = tarfile.TarFile(file, 'w')
    for element in filelist:
        try:
            for file in listdir(element, expression, add_dirs=True):
                tar.add(os.path.join(element, file), file, False)
        except:
            tar.add(element)
    tar.close()

if 'sdist' in sys.argv:
    tar('gluon/env.tar',['applications','VERSION','splashlogo.gif'])


setup(name='web2py',
        version=open("VERSION").read().split()[1],
        description="""full-stack framework for rapid development and prototyping
        of secure database-driven web-based applications, written and
        programmable in Python.""",
        long_description="""
        Everything in one package with no dependencies. Development, deployment,
        debugging, testing, database administration and maintenance of applications can
        be done via the provided web interface. web2py has no configuration files,
        requires no installation, can run off a USB drive. web2py uses Python for the
        Model, the Views and the Controllers, has a built-in ticketing system to manage
        errors, an internationalization engine, works with SQLite, PostgreSQL, MySQL,
        MSSQL, FireBird, Oracle, IBM DB2, Informix, Ingres, sybase and Google App Engine via a
        Database Abstraction Layer. web2py includes libraries to handle
        HTML/XML, RSS, ATOM, CSV, RTF, JSON, AJAX, XMLRPC, WIKI markup. Production
        ready, capable of upload/download streaming of very large files, and always
        backward compatible.
        """,
        author='Massimo Di Pierro',
        author_email='mdipierro@cs.depaul.edu',
        license = 'http://web2py.com/examples/default/license',
        classifiers = ["Development Status :: 5 - Production/Stable"],
        url='http://web2py.com',
        platforms ='Windows, Linux, Mac, Unix,Windows Mobile',
        packages=['gluon',
                  'gluon/contrib',
                  'gluon/contrib/gateways',
                  'gluon/contrib/login_methods',
                  'gluon/contrib/markdown',
                  'gluon/contrib/markmin',
                  'gluon/contrib/memcache',
                  'gluon/contrib/pyfpdf',
                  'gluon/contrib/pymysql',
                  'gluon/contrib/pyrtf',
                  'gluon/contrib/pysimplesoap',
                  'gluon/contrib/simplejson',
                  'gluon/tests',
                    ],
        package_data = {'gluon':['env.tar']},
        scripts = ['mkweb2pyenv','runweb2py'],
        )

