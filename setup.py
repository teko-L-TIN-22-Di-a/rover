from setuptools import setup, find_packages
import importlib.resources

app_name = 'space rover'
description = 'A litte space rover school project.'
version = '0.0.0'

setup(
    name=app_name,
    version= version,
    author='Floindil / atmomic_light',
    tests_require=['pytest'],
    description=description,
    long_description=description,
    url='https://github.com/teko-L-TIN-22-Di-a/rover',
    keywords='development, game, prorotype',
    python_requires='>=3.7, <4',
    packages=find_packages(include='spacerover'),
    entry_points={
        'gui_scripts': [
            'spacerover=spacerover.spacerover:main',
        ]
    }
)
