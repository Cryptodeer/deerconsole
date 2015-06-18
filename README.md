Deerconsole
===========

Python console to test deerwallet api

Install
-----

'''
git clone https://github.com/Cryptodeer/deerconsole
cd deerconsole
python setup.py install
'''

Usage
-----

'''
import deerconsole

pk, pbk, addr = deerconsole.getKeys("seed")
print deerconsole.CreateAccount(pk)

'''