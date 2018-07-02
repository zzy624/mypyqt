from ethereum.utils import *
import bitcoin
import os
key = os.urandom(32)
private_key = encode_hex(key)
public_key = encode_hex(bitcoin.privkey_to_pubkey(key))
address = '0x' + encode_hex(privtoaddr(key))

print(private_key)
print(public_key)
print(address)