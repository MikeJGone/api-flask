import hashlib


def encrypt(password: str):
    h = hashlib.md5()
    h.update(password.encode('utf8'))
    return h.hexdigest()
