#!/usr/bin/env python3
"""
beBriz License Key Generator
=============================
Generates license keys and appends them to licenses/keys.json.

Usage:
    python generate_keys.py --theme luxe-fashion --count 10 --email buyer@example.com

The checksum algorithm is identical to keygen.js and Theme.License in theme.js:
    1. Take prefix = "BEBRIZ-{THEME_CODE}-{RANDOM8}"
    2. sum = sum of (ord(char) * (position + 1)) for each char
    3. mod = sum % 1679616 (36^4)
    4. Convert mod to base36 uppercase, zero-pad to 4 chars
"""

import argparse
import json
import os
import random
import string
from datetime import date

THEME_CODES = {
    'luxe-fashion':  'LUXF',
    'luxe-interior': 'LUXI',
    'luxe-tech':     'LUXT',
    'luxe-gourmet':  'LUXG',
    'pawsome':       'PAWS',
    'vitaboost':     'VITA',
    'brewhaus':      'BREW',
    'pixelmart':     'PIXL',
    'littlejoy':     'LTJY',
    'brilliance':    'BRIL',
    'haus-heim':     'HAUS',
}

CHARS = string.ascii_uppercase + string.digits

KEYS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'licenses', 'keys.json')


def to_base36(n):
    """Convert integer to base36 string (uppercase)."""
    if n == 0:
        return '0'
    digits = []
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while n:
        digits.append(alphabet[n % 36])
        n //= 36
    return ''.join(reversed(digits))


def compute_checksum(prefix):
    """
    Compute 4-char checksum for a key prefix.
    Algorithm must match keygen.js and theme.js exactly.
    """
    total = 0
    for i, ch in enumerate(prefix):
        total += ord(ch) * (i + 1)
    mod = total % 1679616  # 36^4
    h = to_base36(mod).upper()
    return h.zfill(4)


def generate_key(theme_handle, email=''):
    """Generate a single license key."""
    code = THEME_CODES.get(theme_handle)
    if not code:
        raise ValueError(f'Unknown theme: {theme_handle}. Valid: {", ".join(THEME_CODES.keys())}')

    rand = ''.join(random.choices(CHARS, k=8))
    prefix = f'BEBRIZ-{code}-{rand}'
    checksum = compute_checksum(prefix)
    key = f'{prefix}-{checksum}'

    record = {
        'key': key,
        'theme': theme_handle,
        'email': email,
        'domain': None,
        'dev_domain': None,
        'created': date.today().isoformat(),
        'activated': None,
        'status': 'active',
    }
    return key, record


def validate_key(key):
    """Validate a key's format and checksum."""
    import re
    m = re.match(r'^BEBRIZ-([A-Z0-9]{4})-([A-Z0-9]{8})-([A-Z0-9]{4})$', key.strip().upper())
    if not m:
        return False
    prefix = f'BEBRIZ-{m.group(1)}-{m.group(2)}'
    expected = compute_checksum(prefix)
    return m.group(3) == expected


def load_keys():
    """Load existing keys from keys.json."""
    if os.path.exists(KEYS_FILE):
        with open(KEYS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'keys': []}


def save_keys(data):
    """Save keys to keys.json."""
    os.makedirs(os.path.dirname(KEYS_FILE), exist_ok=True)
    with open(KEYS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description='beBriz License Key Generator')
    parser.add_argument('--theme', required=True, choices=list(THEME_CODES.keys()),
                        help='Theme handle')
    parser.add_argument('--count', type=int, default=1,
                        help='Number of keys to generate (default: 1)')
    parser.add_argument('--email', default='',
                        help='Buyer email address')
    args = parser.parse_args()

    data = load_keys()
    generated = []

    for _ in range(args.count):
        key, record = generate_key(args.theme, args.email)
        data['keys'].append(record)
        generated.append(key)

    save_keys(data)

    print(f'\nGenerated {len(generated)} key(s) for {args.theme}:')
    print('-' * 40)
    for k in generated:
        print(f'  {k}')
    print(f'\nSaved to {os.path.abspath(KEYS_FILE)}')

    # Verify all generated keys pass validation
    all_valid = all(validate_key(k) for k in generated)
    print(f'Validation check: {"PASS" if all_valid else "FAIL"}')


if __name__ == '__main__':
    main()
