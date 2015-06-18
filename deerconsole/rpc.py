#!/bin/python
import json
import request
import time
from .utils import *
from .costants import *

#solo local
def rpccall(id, method, params):
	n_time = numint(time.time())
	s_time = numstr(n_time)
	s_id = id
	postreq = { "id":(s_time+s_id), "params":params, "method": method }
	try:
		return requests.post((API_PROTOCOL + "://" + API_ENDPOINT + "/" + API_DEERWALLET_PATH), data=json.dumps(postreq))
	except NameError:
		return NameError