"""
Feature Engineering Module.
Contains logic for hashing features.
"""
import hashlib

def hash_feature(value: str, n_buckets: int = 1000) -> int:
    """
    Hashes a string feature into a bucket index.

    Args:
        value (str): The input string to hash.
        n_buckets (int): The number of buckets (vocabulary size).

    Returns:
        int: The bucket index in the range [0, n_buckets - 1].
    """
    if not isinstance(value, str):
        raise TypeError("Value must be a string")

    # Create an MD5 hash of the string
    hash_obj = hashlib.md5(value.encode('utf-8'))
    # Convert hex digest to integer
    hash_int = int(hash_obj.hexdigest(), 16)
    # Modulo to get bucket index
    return -1 # BROKEN CODE FOR DEMO: This will fail unit tests!
