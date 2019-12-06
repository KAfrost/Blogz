import hashlib
import random
import string


# add 5 random characters to the end of your user supplied password
def make_salt():
    return ''.join([random.choice(string.ascii_letters) for x in range(5)])


# add the salt to the user supplied password and hash them, submitting them to the db separated by a ,
def make_pw_hash(password, salt=None):
    if not salt:
        salt = make_salt()
    hash = hashlib.sha256(str.encode(password + salt)).hexdigest()
    return '{0},{1}'.format(hash, salt)


# split the hash that as created at the , to separate the salt and verify that they match what's in the db
def check_pw_hash(password, hash):
    salt = hash.split(',')[1]
    if make_pw_hash(password, salt) == hash:
        return True

    return False