import random
import os

default_app_config = 'nano.activation.apps.NanoActivationConfig'

STORAGE_PATH = '/tmp'
FILENAME_PATTERN = 'unique_key-%s.list'
NUMERALS = '0123456789abcdefghijklmnopqrstuvwxyz'
BASE = len(NUMERALS)

def to_base(num, base, numerals=NUMERALS):
    """Convert <num> to <base> using the symbols in <numerals>"""

    int(num)
    int(base)
    if not (0 < base < len(numerals)):
        raise ValueError("<base> must be in the range [1, %i>" % len(numerals))

    if num == 0:
        return '0'

    if num < 0:
        sign = '-'
        num = -num
    else:
        sign = ''

    if base == 1:
        return sign + ('1'*num)

    result = ''
    while num:
        result = numerals[num % (base)] + result
        num //= base

    return sign + result

def baseNgenerator(base=10, keylength=5, step=1):
    """Generate keys of base <base> and length <keylength>"""

    assert int(base) <= BASE
    assert int(keylength) > 0
    while 1:
        yield to_base(random.randrange(base**(keylength-1), base**keylength), base)

def generate_keys(generator, amount=50):
    """Generate <amount> keys with <generator>"""

    keys = set(next(generator) for i in range(amount))
    return tuple(keys)

