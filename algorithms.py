# -*- coding: utf-8 -*-
import hashlib, hmac

class Algorithm(object):
    """
    The interface for an algorithm used to sign and verify tokens.
    """
    def prepare_key(self, key):
        """
        Performs necessary validation and conversions on the key and returns
        the key value in the proper format for sign() and verify().
        """
        raise NotImplementedError

    def sign(self, msg, key):
        """
        Returns a digital signature for the specified message
        using the specified key value.
        """
        raise NotImplementedError

    def verify(self, msg, key, sig):
        """
        Verifies that the specified digital signature is valid
        for the specified message and key values.
        """
        raise NotImplementedError



class HMACAlgorithm(Algorithm):
    """
    Performs signing and verification operations using HMAC
    and the specified hash function.
    """
    hash_alg = hashlib.sha256

    def __init__(self):
        self.hash_alg = HMACAlgorithm.hash_alg

    def sign(self, msg, key):
        return hmac.new(key, msg, self.hash_alg).digest()

    def verify(self, msg, key, sig):
        return hmac.compare_digest(sig, self.sign(msg, key))

