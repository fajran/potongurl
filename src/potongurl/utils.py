import re

protocol_re = re.compile(r'^[a-z]+://')

def int_to_base62(i):
    """
    Converts an integer to a base62 string.

    This function is adapted from Django's int_to_base36.
    """
    digits = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    factor = 0
    # Find starting factor
    while True:
        factor += 1
        if i < 62 ** factor:
            factor -= 1
            break
    base62 = []
    # Construct base62 representation
    while factor >= 0:
        j = 62 ** factor
        base62.append(digits[i / j])
        i = i % j
        factor -= 1
    return ''.join(base62)

def get_hash(id):
    return int_to_base62(id)
    
def clean_url(url):
    if url is None:
        return None
    url = url.strip()
    if url == '':
        return None

    if protocol_re.match(url):
        return url
    else:
        return 'http://%s' % url

    
