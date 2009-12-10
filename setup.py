## Copyright (c) 2007-2009 Nathan R. Yergler, Christopher Webber,
##                         Creative Commons

## Permission is hereby granted, free of charge, to any person obtaining
## a copy of this software and associated documentation files (the "Software"),
## to deal in the Software without restriction, including without limitation
## the rights to use, copy, modify, merge, publish, distribute, sublicense,
## and/or sell copies of the Software, and to permit persons to whom the
## Software is furnished to do so, subject to the following conditions:

## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.

from setuptools import setup, find_packages

import sys

setup(
    name = "cc.engine",
    version = "9.1-dev",
    packages = ['cc.engine'],
    namespace_packages = ['cc',],
    
    # scripts and dependencies
    install_requires = [
        'setuptools',
        'cc.license',
        'cc.licenserdf',
        'cc.i18npkg',
        'python-gettext',
        'zope.interface',
        'PasteScript',
        #'repoze.bfg',
        'WebOb',
        'routes',
        'sphinx',
        ],

    # author metadata
    author = 'Christopher Webber',
    author_email = 'cwebber@creativecommons.org',
    description = '',
    license = 'MIT',
    url = 'http://creativecommons.org',
    entry_points = """\
      [paste.app_factory]
      app = cc.engine.app:ccengine_app_factory
      """
    )
