#!/bin/python
from pybitcointools import *
from hashlib import sha256

def checkSig(params):
	if params[0] != "CreateTransaction": 
		tohash = params[1]+str(params[2])+params[3]
		dsig = params[4]
	else:
		tohash = params[1]+params[2]+params[3]+str(params[4])+str(params[5])+params[6]
		dsig = params[7]
	pbk = decode_pubkey(params[1], "hex")
	mhash = sha256(sha256(tohash).digest()).digest()
	o, r, s = decode_sig(dsig)
	return ecdsa_raw_verify(mhash, (o, r, s), pbk)