#!/bin/python
# -*- coding: utf-8 -*-
"""
    deerconsole
    ~~~~~

    :copyright: (c) 2015 by Matteo Assinnata
    :license: MIT, see LICENSE for more details.
"""


from .utils import *
from .costants import *
from .checkSig import checkSig
from pybitcointools import *
from hashlib import sha256
import requests
import json

def ListTransactions(priv, rid="foobar"):
	n_time = numint(time.time())
	s_pbk = privtopub(priv).encode("hex")
	s_time = numstr(n_time)
	s_id = rid
	tohash = s_pbk+s_time+s_id
	mhash = sha256(sha256(tohash).digest() ).digest()
	o, r, s = ecdsa_raw_sign(mhash, priv)
	s_sig = encode_sig(o, r, s)
	postreq = { "id":(s_time+s_id), "params":[ "ListTransactions", s_pbk.encode("hex"), n_time, s_id, s_sig] }
	assert(checkSig(postreq["params"]))
	print json.dumps(postreq) 
	try:
		return requests.post((API_PROTOCOL + "://" + API_ENDPOINT + "/" + API_DEERWALLET_PATH), data=json.dumps(postreq))
	except NameError:
		return NameError