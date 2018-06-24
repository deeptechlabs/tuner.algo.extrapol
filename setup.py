#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Installation script for `orion.algo.gradient_descent`."""
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt', 'r') as f:
    requirements = [r for r in f.read().splitlines() if '==' in r]

with open('requirements_dev.txt', 'r') as f:
    test_requirements = [r for r in f.read().splitlines() if '==' in r]

setup_args = dict(
    name = "orion.algo.extrapol",
    version = "0.1",
    author = "Tobias Domhan, Dendi Suhubdy",
    author_email = "tdomhan@gmail.com, suhubdyd@iro.umontreal.ca",
    description = "Predicting learning curves in python",
    keywords = "python learning curves, prediction",
    long_description=readme,
    license='BSD-3-Clause',
    url='https://github.com/dendisuhubdy/orion.algo.extrapol',
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'OptimizationAlgorithm': [
            'extrapol = orion.algo.extrapol:ExtrapolatingLearningCurves'
            ],
        },
    install_requires = requirements,
    setup_requires=['setuptools'],
    # "Zipped eggs don't play nicely with namespace packaging"
    # from https://github.com/pypa/sample-namespace-packages
    zip_safe=False
    )

setup_args['keywords'] = [
    'Machine Learning',
    'Deep Learning',
    'Distributed',
    'Optimization',
    ]

setup_args['platforms'] = ['Linux']

setup_args['classifiers'] = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
] + [('Programming Language :: Python :: %s' % x)
     for x in '3.6'.split()]

if __name__ == '__main__':
    setup(**setup_args)
