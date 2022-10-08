class Jar:

    # Initializing Capacity of Jar
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    # Returning Number of Cookie's in Jar
    def __str__(self):
        return self.size * "🍪"

    # Adding Cookie's in jar
    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Exceed Capacity")

    # Withdrawing Cookies from jar
    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Not Enough Cookie's")
        self.size -= n

    # Getter for Capacity of Jar
    @property
    def capacity(self):
        return self._capacity

    # Setter set value in Capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


jar = Jar(26)
jar.deposit(24)
jar.withdraw(3)
print(jar)