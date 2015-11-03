from setuptools import setup
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'retsly_python_sdk'))


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='retsly-python-sdk',
    version='0.0.1',
    description="A Python wrapper for the Retsly API (https://rets.ly)",
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='retsly python sdk',
    url='https://github.com/retsly/python-sdk',
    author='Retsly Software Inc.',
    author_email='support@rets.ly',
    license='MIT',
    packages=[
        'retsly_python_sdk'
    ],
    install_requires=[
        'requests',
        'jsonurl'
    ]
)