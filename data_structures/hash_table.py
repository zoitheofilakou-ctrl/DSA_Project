class EmailRegistry:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, email):
        # simple hash - sum of characters mod size
        return sum(ord(ch) for ch in email) % self.size

    def add_email(self, email):
        index = self.hash_function(email)
        for e in self.table[index]:
            if e == email:
                print(f"email '{email}' already exists")
                return False
        self.table[index].append(email)
        print(f" Register: {email}")
        return True

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# ------------------------Implementation Example ---------------------------------

registry = EmailRegistry(10)

registry.add_email("anna@gmail.com")
registry.add_email("nikos@yahoo.com")
registry.add_email("maria@gmail.com")
registry.add_email("anna@gmail.com")  #double email

print("\nHash Table contents:")
registry.display()
