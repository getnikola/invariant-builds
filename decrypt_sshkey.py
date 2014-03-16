#!/usr/bin/env python
from Crypto.Cipher import AES
import os

obj = AES.new(os.environ['ENCKEY'])

with open('./SSHKEY', 'rb') as fh:
    encrypted = fh.read()

decrypted = obj.decrypt(encrypted)

with open('./id_rsa', 'wb') as fh:
    # The last bytes are padding \0s.
    fh.write(decrypted[:-5])
