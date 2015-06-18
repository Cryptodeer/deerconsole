# -*- coding: utf-8 -*-
"""
    deerconsole
    ~~~~~

    :copyright: (c) 2015 by Matteo Assinnata
    :license: MIT, see LICENSE for more details.
"""

from pybitcoin import BitcoinPrivateKey, bin_double_sha256
import binascii
from hashlib import sha256
from binascii import hexlify, unhexlify
import time
import math
from pybitcointools import *
import logging

def logme(data, path="/etc/dnet/data/uwsgi/json.log"):
	logging.basicConfig(filename=path,level=logging.DEBUG)
	logging.debug(data)
	return "done"
	
def foosign(msg, priv):
	v, r, s = ecdsa_raw_sign(msg, priv)
	return r, s, v

def reverse_hash(hash, hex_format=True):
    """ hash is in hex or binary format
    """
    if not hex_format:
        hash = hexlify(hash) 
    return "".join(reversed(hash))


# digest object for double bin hash
class BinHash256:
	def __init__(self, data):
		bindoublehash = bin_double_sha256(data) 
		reversedhash = reverse_hash(bindoublehash)
		self.dgst = reversedhash
	def printf(self):
		print "hexdgst", hexlify(self.dgst)
	def digest(self):
		return self.dgst

class TetraPK(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 0x41

def numstr(numeric):
	return str(int(math.floor(numeric)))

def numint(numeric):
	return int(math.floor(numeric))

def bin_pbk(data):
	return extract_bin_bitcoin_pubkey(data)