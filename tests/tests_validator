import sys
import os
import pytest

# Manually add the project root to the Python path
# This allows 'pytest' to see the 'src' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.validator import RecordValidator

@pytest.fixture
def validator():
    """Provides a fresh RecordValidator instance for each test."""
    return RecordValidator()

def test_valid_standard_id(validator):
    """Test IDs with standard formatting."""
    assert validator.is_valid_id("123456") is True
    assert validator.is_valid_id("12-34-56") is True
    assert validator.is_valid_id("12 34 56") is True

def test_invalid_id_length(validator):
    """Test IDs that are too short or too long."""
    assert validator.is_valid_id("12345") is False
    assert validator.is_valid_id("1234567") is False

def test_non_numeric_input(validator):
    """Test IDs that contain letters."""
    assert validator.is_valid_id("ABCDEF") is False
    assert validator.is_valid_id("12-34-XY") is False

def test_empty_string(validator):
    """Test empty input handling."""
    assert validator.is_valid_id("") is False
