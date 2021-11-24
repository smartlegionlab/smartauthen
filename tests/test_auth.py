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


class TestSmartAuth:
    def test_make_key(self, smart_auth, context):
        assert smart_auth.make_key(login=context.login, secret=context.secret) == context.key

    def test_check(self, smart_auth, context):
        assert smart_auth.check(login=context.login, secret=context.secret, key=context.key)

    def test__get_hash(self, smart_auth):
        assert smart_auth._get_hash('Py') != smart_auth._get_hash('Yp')
        assert smart_auth._get_hash('Py') == smart_auth._get_hash('Py')
