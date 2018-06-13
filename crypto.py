#!/usr/bin/env python
import rsa


(pubkey1, privkey1) = rsa.newkeys(512)
(pubkey2, privkey2) = rsa.newkeys(512)


# first user get the pubkey form second user
message1 = b"-100000000000000.000000000000000000000000000000000000"
crypto = rsa.encrypt(message1, pubkey2)
message = rsa.decrypt(crypto, privkey2)
print("first user: %s" % message1)


# second user get the pubkey form first user
message2 = b"+1000000.00000000"
crypto = rsa.encrypt(message2, pubkey1)
message = rsa.decrypt(crypto, privkey1)
print("second user: %s" % message2)
