import hashlib


class Hasher:
    def __init__(self, algorithm='sha256'):
        self.algorithm = algorithm

    def hash_string(self, string):
        """Hashes a string using the specified algorithm."""
        hasher = hashlib.new(self.algorithm)
        hasher.update(string.encode('utf-8'))
        return hasher.hexdigest()
