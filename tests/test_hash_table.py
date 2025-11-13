import pytest
from data_structures.hash_table import EmailRegistry


@pytest.fixture
def registry():
    """Fixture to create a new EmailRegistry for testing."""
    return EmailRegistry(size=5)


# Test: Ensures a new email is added successfully.
def test_add_email_success(registry):
    """Add a new email and verify it's stored in the correct bucket."""
    result = registry.add_email("user@example.com")
    assert result is True
    assert registry.exists("user@example.com") is True


#  Test: Prevents adding duplicate emails.
def test_add_duplicate_email(registry):
    """Try adding the same email twice and confirm the second attempt fails."""
    registry.add_email("john@example.com")
    result = registry.add_email("john@example.com")
    assert result is False
    assert registry.exists("john@example.com") is True


# Test: Handles collisions correctly.
def test_collision_handling(registry):
    """Different emails may map to the same bucket but both should be stored."""
    # Force a collision by using a small table size
    email1 = "a@example.com"
    email2 = "f@example.com"  # likely same hash index with small size
    registry.add_email(email1)
    registry.add_email(email2)
    assert registry.exists(email1)
    assert registry.exists(email2)


# Test: Verifies that hash_function returns valid indices.
def test_hash_function_within_range(registry):
    """Ensure that hash index is always within valid range 0..size-1."""
    index = registry.hash_function("zoi@example.com")
    assert 0 <= index < registry.size


#  Test: Displays table correctly after multiple insertions.
def test_display_output(registry):
    """Check that display() runs without errors after adding items."""
    emails = ["a@x.com", "b@x.com", "c@x.com"]
    for e in emails:
        registry.add_email(e)
    # Simply ensure display prints without exceptions
    registry.display()
    for e in emails:
        assert registry.exists(e)
