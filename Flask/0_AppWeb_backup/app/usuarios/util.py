import os, hashlib, binascii



# Inspirado en -> https://www.vitoshacademy.com/hashing-passwords-in-python/


def hash_password(password):
    """Obtiene el código Hash del password para grabarlo"""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash)     # devuelve bytes


def comprobar_password(password, password_almacenado):
    """Comprueba el password introducido con el almacenado"""
    password_almacenado = password_almacenado.decode('ascii')
    salt = password_almacenado[:64]
    password_almacenado = password_almacenado[64:]
    password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(password_hash).decode('ascii')
    return pwdhash == password_almacenado
