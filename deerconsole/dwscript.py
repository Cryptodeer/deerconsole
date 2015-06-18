

rpc_account="getnewaddress"
rpc_listtransaction="listtransactions"
rpc_accounts="listaccounts"
rpc_getbalance="listaccounts"
rpc_createtransaction="sendmany"
from .rpc import rpccall
from .checkSig import checksig
import json

def process(req):
	if !checksig(req["params"]):
		return False
	return rpccall(req["id"], "dwskipchecksig", req["params"])