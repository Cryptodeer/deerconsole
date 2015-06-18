# -*- coding: utf-8 -*-
"""
    deerconsole
    ~~~~~

    :copyright: (c) 2015 by Matteo Assinnata
    :license: MIT, see LICENSE for more details.
"""
 
from pybitcointools import *
from hashlib import sha256 
 
def getKeys(seed):
	upcat = seed
	pkey = sha256(sha256(upcat).digest()).digest()
	pk = pkey #encode_privkey(pkey, "wif", 65)
	pbk = privtopub(pk)
	addr = pubkey_to_address(pbk)
	return pk, pbk, addr