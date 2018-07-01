# -*-coding:utf-8-*-

import sys,time
# import cgitb
# cgitb.enable( format = 'text')
import pbkdf2
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
from mypyqt.ui.pyui.ui_account import Ui_account
import json
import os
import random
from ethereum.tools import keys
# from pyethapp.accounts import Account
from ethereum.utils import privtopub  # this is different  than the one used in devp2p.crypto
from ethereum.utils import sha3, is_string, decode_hex, remove_0x_head,encode_hex
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from eth_utils.hexadecimal import decode_hex



class MyAccount(QDialog, Ui_account):

    def __init__(self):
        super(MyAccount, self).__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_genAddress_clicked(self):
        a = Account.new("123")
        print("address:",a.address)
        print("keystore:",a.keystore)
        print("privkey",a.privkey)
        print("pubkey",a.pubkey)



# def mk_privkey(seed):
#     return sha3(seed)
#
#
def mk_random_privkey():
    k = hex(random.getrandbits(256))[2:-1].zfill(64)
    assert len(k) == 64
    print(decode_hex(k))
    # return k.decode('hex')
    return decode_hex(k)
#
# def aes_ctr_encrypt(text, key, params):
#     iv = big_endian_to_int(decode_hex(params["iv"]))
#     ctr = Counter.new(128, initial_value=iv, allow_wraparound=True)
#     mode = AES.MODE_CTR
#     encryptor = AES.new(key, mode, counter=ctr)
#     return encryptor.encrypt(text)
#
#
# def aes_ctr_decrypt(text, key, params):
#     iv = big_endian_to_int(decode_hex(params["iv"]))
#     ctr = Counter.new(128, initial_value=iv, allow_wraparound=True)
#     mode = AES.MODE_CTR
#     encryptor = AES.new(key, mode, counter=ctr)
#     return encryptor.decrypt(text)
#
# def aes_mkparams():
#     return {"iv": encode_hex(os.urandom(16))}
#
# def mk_pbkdf2_params():
#     params = PBKDF2_CONSTANTS.copy()
#     params['salt'] = encode_hex(os.urandom(16))
#     return params
#
# def pbkdf2_hash(val, params):
#     assert params["prf"] == "hmac-sha256"
#     return pbkdf2.PBKDF2(val, decode_hex(params["salt"]), params["c"],
#                          SHA256).read(params["dklen"])
#
# ciphers = {
#     "aes-128-ctr": {
#         "encrypt": aes_ctr_encrypt,
#         "decrypt": aes_ctr_decrypt,
#         "mkparams": aes_mkparams
#     }
# }
# kdfs = {
#     "pbkdf2": {
#         "calc": pbkdf2_hash,
#         "mkparams": mk_pbkdf2_params
#     }
# }
#
# def make_keystore_json(priv, pw, kdf="pbkdf2", cipher="aes-128-ctr"):
#     # Get the hash function and default parameters
#     if kdf not in kdfs:
#         raise Exception("Hash algo %s not supported" % kdf)
#     kdfeval = kdfs[kdf]["calc"]
#     kdfparams = kdfs[kdf]["mkparams"]()
#     # Compute derived key
#     derivedkey = kdfeval(pw, kdfparams)
#     # Get the cipher and default parameters
#     if cipher not in ciphers:
#         raise Exception("Encryption algo %s not supported" % cipher)
#     encrypt = ciphers[cipher]["encrypt"]
#     cipherparams = ciphers[cipher]["mkparams"]()
#     # Produce the encryption key and encrypt
#     enckey = derivedkey[:16]
#     c = encrypt(priv, enckey, cipherparams)
#     # Compute the MAC
#     mac = sha3(derivedkey[16:32] + c)
#     # Make a UUID
#     u = encode_hex(os.urandom(16))
#     if sys.version_info.major == 3:
#         u = bytes(u, 'utf-8')
#     uuid = b'-'.join((u[:8], u[8:12], u[12:16], u[16:20], u[20:]))
#     # Return the keystore json
#     return {
#         "crypto": {
#             "cipher": cipher,
#             "ciphertext": encode_hex(c),
#             "cipherparams": cipherparams,
#             "kdf": kdf,
#             "kdfparams": kdfparams,
#             "mac": encode_hex(mac),
#             "version": 1
#         },
#         "id": uuid,
#         "version": 3
#     }

class Account(object):

    """Represents an account.

    :ivar keystore: the key store as a dictionary (as decoded from json)
    :ivar locked: `True` if the account is locked and neither private nor public keys can be
                  accessed, otherwise `False`
    :ivar path: absolute path to the associated keystore file (`None` for in-memory accounts)
    """

    def __init__(self, keystore, password=None, path=None):
        self.keystore = keystore
        try:
            self._address = self.keystore['address'].decode('hex')
        except KeyError:
            self._address = None
        self.locked = True
        if password is not None:
            self.unlock(password)
        if path is not None:
            self.path = os.path.abspath(path)
        else:
            self.path = None

    @classmethod
    def new(cls, password, key=None, uuid=None, path=None):
        """Create a new account.

        Note that this creates the account in memory and does not store it on disk.

        :param password: the password used to encrypt the private key
        :param key: the private key, or `None` to generate a random one
        :param uuid: an optional id
        """
        if key is None:
            key = mk_random_privkey()
        keystore = keys.make_keystore_json(key, password)
        keystore['id'] = uuid
        return Account(keystore, password, path)

    @classmethod
    def load(cls, path, password=None):
        """Load an account from a keystore file.

        :param path: full path to the keyfile
        :param password: the password to decrypt the key file or `None` to leave it encrypted
        """
        with open(path) as f:
            keystore = json.load(f)
        if not keys.check_keystore_json(keystore):
            raise ValueError('Invalid keystore file')
        return Account(keystore, password, path=path)

    def dump(self, include_address=True, include_id=True):
        """Dump the keystore for later disk storage.

        The result inherits the entries `'crypto'` and `'version`' from `account.keystore`, and
        adds `'address'` and `'id'` in accordance with the parameters `'include_address'` and
        `'include_id`'.

        If address or id are not known, they are not added, even if requested.

        :param include_address: flag denoting if the address should be included or not
        :param include_id: flag denoting if the id should be included or not
        """
        d = {}
        d['crypto'] = self.keystore['crypto']
        d['version'] = self.keystore['version']
        if include_address and self.address is not None:
            d['address'] = self.address.encode('hex')
        if include_id and self.uuid is not None:
            d['id'] = self.uuid
        return json.dumps(d)

    def unlock(self, password):
        """Unlock the account with a password.

        If the account is already unlocked, nothing happens, even if the password is wrong.

        :raises: :exc:`ValueError` (originating in ethereum.keys) if the password is wrong (and the
                 account is locked)
        """
        if self.locked:
            self._privkey = keys.decode_keystore_json(self.keystore, password)
            self.locked = False
            self.address  # get address such that it stays accessible after a subsequent lock

    def lock(self):
        """Relock an unlocked account.

        This method sets `account.privkey` to `None` (unlike `account.address` which is preserved).
        After calling this method, both `account.privkey` and `account.pubkey` are `None.
        `account.address` stays unchanged, even if it has been derived from the private key.
        """
        self._privkey = None
        self.locked = True

    @property
    def privkey(self):
        """The account's private key or `None` if the account is locked"""
        if not self.locked:
            return self._privkey
        else:
            return None

    @property
    def pubkey(self):
        """The account's public key or `None` if the account is locked"""
        if not self.locked:
            return privtopub(self.privkey)
        else:
            return None

    @property
    def address(self):
        """The account's address or `None` if the address is not stored in the key file and cannot
        be reconstructed (because the account is locked)
        """
        if self._address:
            pass
        elif 'address' in self.keystore:
            self._address = self.keystore['address'].decode('hex')
        elif not self.locked:
            self._address = keys.privtoaddr(self.privkey)
        else:
            return None
        return self._address

    @property
    def uuid(self):
        """An optional unique identifier, formatted according to UUID version 4, or `None` if the
        account does not have an id
        """
        try:
            return self.keystore['id']
        except KeyError:
            return None

    @uuid.setter
    def uuid(self, value):
        """Set the UUID. Set it to `None` in order to remove it."""
        if value is not None:
            self.keystore['id'] = value
        elif 'id' in self.keystore:
            self.keystore.pop('id')

    def sign_tx(self, tx):
        """Sign a Transaction with the private key of this account.

        If the account is unlocked, this is equivalent to ``tx.sign(account.privkey)``.

        :param tx: the :class:`ethereum.transactions.Transaction` to sign
        :raises: :exc:`ValueError` if the account is locked
        """
        if self.privkey:
            log.info('signing tx', tx=tx, account=self)
            tx.sign(self.privkey)
        else:
            raise ValueError('Locked account cannot sign tx')

    def __repr__(self):
        if self.address is not None:
            # address = self.address.encode('hex')
            address = encode_hex(self.address)
        else:
            address = '?'
        return '<Account(address={address}, id={id})>'.format(address=address, id=self.uuid)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MyAccount()
    dlg.show()
    try:
        app.exec_()
    except Exception as e:
        print(e)
