# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
"""Smart, simple, lightweight, secure cross-platform
authentication for any application."""
import hashlib


class HashGenerator:
    """
    A class for generating hashes using the SHA-3 512 algorithm.

    Methods:
        generate(text: str) -> str:
            Generates a hash for the given text.
    """

    @classmethod
    def generate(cls, text: str) -> str:
        """
        Generates an SHA-3 512 hash for the given text.

        Parameters:
            text (str): The input text for which the hash will be generated.

        Returns:
            str: The hash in hexadecimal format.
        """
        text = str(text)
        sha = hashlib.sha3_512(text.encode('utf-8'))
        return sha.hexdigest()


class SmartAuth:
    """
    Authentication for any application.

    Smart, simple, lightweight, and secure cross-platform
    authentication for any application.
    """
    step = 15

    @classmethod
    def make_key(cls, login: str, secret: str) -> str:
        """
        Creates a public key linked to the login and secret phrase.

        This method generates a public key by hashing the login and secret phrase,
        and applying a series of transformations to enhance security.

        Parameters:
            login (str): The login or any word or phrase.
            secret (str): Any word or phrase used as a secret.

        Returns:
            str: The generated public key.
        """
        login_hash = cls._get_hash(text=login)
        secret_hash = cls._get_hash(text=secret)
        all_hash = cls._get_hash(text=login_hash + secret_hash)
        for _ in range(cls.step):
            temp_hash = cls._get_hash(all_hash)
            all_hash = cls._get_hash(all_hash + temp_hash + secret_hash)
        return cls._get_hash(all_hash)

    def check(self, login: str, secret: str, key: str) -> bool:
        """
        Checks a pair of login and secret phrase against the public key.

        If the provided login and secret phrase match those used to generate
        the public key, this method will return True.

        Parameters:
            login (str): The login or any word or phrase.
            secret (str): Any word or phrase used as a secret.
            key (str): The public key to compare against.

        Returns:
            bool: True if the login and secret match the public key, False otherwise.

        Example:
            >>> public_key = SmartAuth().make_key("login", "secret")
            >>> is_valid = SmartAuth().check("login", "secret", public_key)
            >>> print(is_valid)
            True
        """
        return self.make_key(login=login, secret=secret) == key

    @staticmethod
    def _get_hash(text: str) -> str:
        """
        Hashes a string using the HashGenerator.

        This method is a static utility that generates a hash for the given text.

        Parameters:
            text (str): The text to be hashed.

        Returns:
            str: The resulting hash string.
        """
        return HashGenerator.generate(text=text)
