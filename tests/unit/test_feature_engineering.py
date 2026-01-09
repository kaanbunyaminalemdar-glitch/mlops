import pytest
from src.feature_engineering import hash_feature

def test_hash_feature_deterministic():
    """Test that the hashing function returns the same value for the same input."""
    val = "test_string"
    assert hash_feature(val, 100) == hash_feature(val, 100)

def test_hash_feature_range():
    """Test that the hashing function returns values within range."""
    val = "another_string"
    buckets = 50
    result = hash_feature(val, buckets)
    assert 0 <= result < buckets

def test_hash_feature_empty():
    """Test hashing an empty string."""
    assert 0 <= hash_feature("", 10) < 10

def test_invalid_input():
    """Test that invalid input raises TypeError."""
    with pytest.raises(TypeError):
        hash_feature(123)
