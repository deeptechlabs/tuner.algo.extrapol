#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Installation script for `orion.algo.gradient_descent`."""
from setuptools import setup

setup_args = dict(
    name = "orion.algo.extrapol",
    version = "0.1",
    author = "Tobias Domhan, Dendi Suhubdy",
    author_email = "tdomhan@gmail.com, suhubdyd@iro.umontreal.ca",
    install_requires = ['numpy', 'docutils>=0.3', 'setuptools', 'matplotlib'],
    description = ("Predicting learning curves in python"),
    keywords = "python learning curves, prediction",
    url = "http://packages.python.org/orion.algo.extrapol",
    long_description="",
    name='orion.algo.extrapol',
    version=0.1,
    description="Implement extrapolating learning curves",
    license='BSD-3-Clause',
    url='https://github.com/dendisuhubdy/orion.algo.extrapol',
    packages=['orion.algo'],
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'OptimizationAlgorithm': [
            'extrapol = orion.algo.extrapol:ExtrapolatingLearningCurves'
            ],
        },
    install_requires=['orion.core'],
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
