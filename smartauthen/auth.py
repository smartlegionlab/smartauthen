# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# smartlegiondev@gmail.com
# --------------------------------------------------------
"""Smart, simple, lightweight, secure cross-platform
authentication for any application."""
import hashlib


class SmartAuth:
    """
    Authentication for any application.

    Smart, simple, lightweight, secure cross-platform
    authentication for any application.
    """
    def __init__(self):
        self._hash_gen = hashlib.sha3_512
        self._step = 15

    def make_key(self, login, secret):
        """
        Creates a public key linked to the login and secret phrase.
        :param login: <str> - login or any word or phrase.
        :param secret: <str> - any word or phrase.
        :return: <str> - public key.
        """
        login_hash = self._get_hash(text=login)
        secret_hash = self._get_hash(text=secret)
        all_hash = self._get_hash(text=login_hash + secret_hash)
        for _ in range(self._step):
            temp_hash = self._get_hash(all_hash)
            all_hash = self._get_hash(all_hash + temp_hash + secret_hash)
        return self._get_hash(all_hash)

    def check(self, login, secret, key):
        """
        Checking a pair of login + secret phrase for
        comparison with the public key.

        - If the pair login + secret phrase are the same,
         what were used to generate the public key,
         will return True.

        :param login: <str> - login or any word or phrase.
        :param secret: <str> - any word or phrase.
        :param key: <str> - public key.
        :return: <bool> - logical check status.
        """
        return self.make_key(login=login, secret=secret) == key

    def _get_hash(self, text):
        """
        Hashes a string.

        :param text: <str> text.
        :return: <str> - Hash string.
        """
        sha = self._hash_gen(text.encode('utf-8'))
        return sha.hexdigest()
