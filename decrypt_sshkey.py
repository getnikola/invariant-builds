#!/usr/bin/env python
from Crypto.Cipher import AES
import os

obj = AES.new(os.environ['ENCKEY'])

with open('./SSHKEY', 'rb') as fh:
    encrypted = fh.read()

decrypted = obj.decrypt(encrypted)

with open('./id_rsa', 'wb') as fh:
    # The last byte is a padding \0.
    fh.write(decrypted[:-1])
