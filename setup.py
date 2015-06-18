"""
deerconsole
==============

"""

from setuptools import setup, find_packages

setup(
    name='deerconsole',
    version='0.8.3',
    url='https://github.com/Cryptodeer/deerconsole',
    license='MIT',
    author='Matteo Assinnata',
    author_email='matteo@assinnata.com',
    description=("deerapi server"),
    keywords='Tetra Cryptodeer cryptocurrency',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'ecdsa==0.11',
        'requests>=2.4.3',
        'pybitcointools>=1.1.28',
        'utilitybelt>=0.1.7'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
