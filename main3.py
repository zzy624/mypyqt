from ethereum.utils import *
import bitcoin
import os,json
from ethereum.tools import keys
key = os.urandom(32)
private_key = encode_hex(key)
public_key = encode_hex(bitcoin.privkey_to_pubkey(key))
address = '0x' + encode_hex(privtoaddr(key))
print(private_key)
print(public_key)
print(address)
keyStore = keys.make_keystore_json(decode_hex(private_key),"123")
print(keyStore)
print(keys.check_keystore_json(keyStore))