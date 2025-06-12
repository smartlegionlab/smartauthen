# smartauthen <sup>v0.2.4</sup>

***

[![PyPI Downloads](https://static.pepy.tech/badge/smartauthen)](https://pepy.tech/projects/smartauthen)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartauthen)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartauthen?label=pypi%20downloads)](https://pypi.org/project/smartauthen/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartauthen)](https://github.com/smartlegionlab/smartauthen/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartauthen)](https://github.com/smartlegionlab/smartauthen/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/smartauthen)](https://pypi.org/project/smartauthen)
[![PyPI - Format](https://img.shields.io/pypi/format/smartauthen)](https://pypi.org/project/smartauthen)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smartauthen?style=social)](https://github.com/smartlegionlab/smartauthen/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smartauthen?style=social)](https://github.com/smartlegionlab/smartauthen/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smartauthen?style=social)](https://github.com/smartlegionlab/smartauthen/)

***

## Short description:

___smartauthen___ - Smart, simple, lightweight, secure cross-platform authentication for any application.

***

Author and developer: ___A.A. Suvorov.___

***

## Supported:

- Linux: All.
- Windows: 7/8/10/11?.
- Termux (Android).

***

## What's new?

___smartauthen v0.2.4___

Code and documentation improvements:

- Enabled the class to be used without creating an instance.
- Added documentation to the code for better understanding.
- Updated the documentation section in the README.
- Simplified the process of enhancing the security of the public key.

The code is now more user-friendly and secure!


***

## Description:

___smartauthen___ - Smart, simple, lightweight, secure cross-platform authentication for any application.

- Use simple yet very reliable and secure authentication in any of your applications.


- Avoid passwords when registering and authenticating in your applications. It is difficult for a user to remember passwords,
therefore, users use either short passwords or light passwords, which plays into the hands of cybercriminals.
The secret phrase is difficult to find and easy to remember. At the moment there are no rainbow tables of secret phrases,
since this is unrealistic. For example, I can use when registering as a secret
Quatrain phrases from your favorite song. 


- It makes no difference to your authentication system how long the secret phrase is, in any case, you will receive only
fixed-length key as a string. 


- Let your users register with an easy-to-remember secret phrase that the user
will be easy to remember, but an attacker will not be able to pick it up.


- Store only login and public key in your databases,
if your database gets compromised,
an attacker will not gain access to user accounts
and will not be able to use public keys for authentication in any way,
after all, by the public key, he will not be able to find out the secret phrase in any way. 

Possibilities: 

- Generation of a public key linked to a pair of login + secret phrase.
- Checking user data login + secret phrase + public key.
- Regulation of complexity in the generation of a public key.

Attention! 

- The public key for the login + secret phrase pair will always be the same.


- With any change in the login or secret phrase, the key will change, therefore
if the user changes his username or passphrase, the key needs to be regenerated.


- If your system can use the same logins for registration and authentication,
use something else, unique, to generate the public key, such as a unique identifier.


- If you change the value of the `step` attribute in the SmartAuth object, the key for the login + secret phrase pair will also change. 
Always use the same value for this attribute. The higher the value of this attribute, the more secure the public key. 


Usage:

- When registering, you will receive a login and a secret phrase from the user.


- Based on the data received, generate a public key for further storage, paired with a login.
If your system can use the same logins for registration and authentication,
use something else, unique, to generate the public key, such as a unique identifier. 


- When authenticating a user, you are asked to enter a login and a secret phrase.


- Checking the data. 


(During verification, a public key is first generated based on the received data, 
compared with the stored key, and a boolean value of the key comparison is returned.) 

***

## Install and Use:

### Install:

- `pip install smartauthen`

#### Use:

```python
from smartauthen import SmartAuth

smart_auth = SmartAuth()

login = 'login'
secret = 'secret'

key = smart_auth.make_key(login, secret)

# True since the login + secret phrase is correct
print(smart_auth.check(login, secret, key))  # True

secret = 'secret2'

# False because the secret phrase is incorrect
print(smart_auth.check(login=login, secret=secret, key=key))  # False

```

***

## For the developer:


#### For run tests:

- `pip install pytest`
- `pytest -v`

#### For run tests coverage:

- `pip install pytest-cov`
- `pytest --cov --cov-report=html`

#### Test coverage:

Coverage 100% !!!

![coverage img](https://github.com/smartlegionlab/smartauth/raw/master/data/images/smartauthen.png)

#### Building and publishing a package:

- `python -m build`

Or outdated method:

- `python setup.py sdist bdist_wheel`

- `twine upload dist/*`


***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
