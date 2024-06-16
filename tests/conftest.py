# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from collections import namedtuple

import pytest

from smartauthen import SmartAuth


@pytest.fixture(name='context')
def context():
    keys = (
        'login',
        'secret',
        'key',
    )
    Context = namedtuple('Context', keys)
    login = 'login'
    secret = 'secret'
    key = '15795be051670afec910bc980189a6011f9f184dea4bbbe4e005e4ca89f3' \
          '18bea963b1a362167b4de909a4f57e1895298f79346068487881c8c969dce4fe909f'
    kwargs = dict(
        login=login,
        secret=secret,
        key=key,
    )
    return Context(**kwargs)


@pytest.fixture(name='smart_auth')
def smart_auth():
    return SmartAuth()
