# -------------------- Hash Table (Email Registry) --------------------

class EmailRegistry:
    """A simple hash table implementation for storing unique email addresses."""

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Separate chaining for collisions

    def hash_function(self, email):
        """Compute hash index using sum of ASCII values modulo table size."""
        return sum(ord(ch) for ch in email) % self.size

    def add_email(self, email):
        """Add a new email if not already present."""
        index = self.hash_function(email)
        bucket = self.table[index]

        if email in bucket:
            print(f"Email '{email}' already exists.")
            return False

        bucket.append(email)
        print(f"Register: {email}")
        return True

    def exists(self, email):
        """Check if an email is already registered."""
        index = self.hash_function(email)
        return email in self.table[index]

    def display(self):
        """Display the hash table buckets."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")
